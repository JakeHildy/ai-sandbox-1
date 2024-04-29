import { config } from "dotenv";

import { ChatOpenAI, OpenAIEmbeddings } from "@langchain/openai";
import { RecursiveCharacterTextSplitter } from "langchain/text_splitter";
import { CheerioWebBaseLoader } from "langchain/document_loaders/web/cheerio";

import {
  ChatPromptTemplate,
  MessagesPlaceholder,
} from "@langchain/core/prompts";
import { StringOutputParser } from "@langchain/core/output_parsers";

import { createRetrievalChain } from "langchain/chains/retrieval";
import { createStuffDocumentsChain } from "langchain/chains/combine_documents";
import { createHistoryAwareRetriever } from "langchain/chains/history_aware_retriever";

import { MemoryVectorStore } from "langchain/vectorstores/memory";

import boxen from "./boxen.js";
import rl from "./readline.js";

config();

const chatModel = new ChatOpenAI({});
const outputParser = new StringOutputParser();
const splitter = new RecursiveCharacterTextSplitter();
const embeddings = new OpenAIEmbeddings();

// 1. LOAD IN SOME DATA AND CREATE DOCS
const loader = new CheerioWebBaseLoader(
  //   "https://en.wikipedia.org/wiki/Random_number_generation"
  "https://js.langchain.com/docs/get_started/quickstart"
);
// load
const docs = await loader.load();
// split
const splitDocs = await splitter.splitDocuments(docs);
// store as vector with retriever
const vectorstore = await MemoryVectorStore.fromDocuments(
  splitDocs,
  embeddings
);
const retriever = vectorstore.asRetriever();
// console.log(splitDocs[0].metadata);

// const prompt =
//   ChatPromptTemplate.fromTemplate(`Answer the following question based only on the provided context:

// <context>
// {context}
// </context>

// Question: {input}`);

const historyAwarePrompt = ChatPromptTemplate.fromMessages([
  new MessagesPlaceholder("chat_history"),
  ["user", "{input}"],
  [
    "user",
    "Given the above conversation, generate a search query to look up in order to get information relevant to the conversation",
  ],
]);

const historyAwareRetrievalPrompt = ChatPromptTemplate.fromMessages([
  [
    "system",
    "Answer the user's questions based on the below context:\n\n{context}",
  ],
  new MessagesPlaceholder("chat_history"),
  ["user", "{input}"],
]);

const historyAwareRetrieverChain = await createHistoryAwareRetriever({
  llm: chatModel,
  retriever,
  rephrasePrompt: historyAwarePrompt,
});
// const documentChain = await createStuffDocumentsChain({
//   llm: chatModel,
//   prompt,
// });
const historyAwareCombineDocsChain = await createStuffDocumentsChain({
  llm: chatModel,
  prompt: historyAwareRetrievalPrompt,
});
const conversationalRetrievalChain = await createRetrievalChain({
  retriever: historyAwareRetrieverChain,
  combineDocsChain: historyAwareCombineDocsChain,
});

// (Could call it this way) ===
// import { Document } from "@langchain/core/documents";

// await documentChain.invoke({
//   input: "what is LangSmith?",
//   context: [
//     new Document({
//       pageContent:
//         "LangSmith is a platform for building production-grade LLM applications.",
//     }),
//   ],
// });
// ============================

// const retrievalChain = await createRetrievalChain({
//   combineDocsChain: documentChain,
//   retriever,
// });

// === basic chat
// const prompt = ChatPromptTemplate.fromMessages([
//   [
//     "system",
//     "You are an expert on hockey history. Give results that include lots of stats. ",
//   ],
//   ["user", "{input}"],
// ]);

// const chain = prompt.pipe(chatModel).pipe(outputParser);

const loop = () => {
  rl.question(">> ", async (content) => {
    // const result = await chain.invoke({
    //   input: content,
    // });
    // const result = await retrievalChain.invoke({
    //   input: content,
    // });
    const result2 = await conversationalRetrievalChain.invoke({
      // chat_history: [
      //   new HumanMessage("Can LangSmith help test my LLM applications?"),
      //   new AIMessage("Yes!"),
      // ],
      input: content,
    });
    // console.log(result);
    boxen(result2.answer, "Open AI", "ai");
    loop();
  });
};

loop();
