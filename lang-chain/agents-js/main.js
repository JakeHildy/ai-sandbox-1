import { config } from "dotenv";

import { createRetrieverTool } from "langchain/tools/retriever";
import { CheerioWebBaseLoader } from "langchain/document_loaders/web/cheerio";
import { TavilySearchResults } from "@langchain/community/tools/tavily_search";
import { ChatOpenAI, OpenAIEmbeddings } from "@langchain/openai";
import { RecursiveCharacterTextSplitter } from "langchain/text_splitter";
import { MemoryVectorStore } from "langchain/vectorstores/memory";
import { HumanMessage, AIMessage } from "@langchain/core/messages";

import { pull } from "langchain/hub";
import { createOpenAIFunctionsAgent, AgentExecutor } from "langchain/agents";

config();

const splitter = new RecursiveCharacterTextSplitter();
const embeddings = new OpenAIEmbeddings();

// 1. LOAD IN SOME DATA AND CREATE DOCS
const loader = new CheerioWebBaseLoader(
  "https://docs.smith.langchain.com/user_guide"
  //   "https://en.wikipedia.org/wiki/Random_number_generation"
  //   "https://js.langchain.com/docs/get_started/quickstart"
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

const retrieverTool = await createRetrieverTool(retriever, {
  name: "langsmith_search",
  description:
    "Search for information about LangSmith. For any questions about LangSmith, you must use this tool!",
});
const searchTool = new TavilySearchResults();

const tools = [retrieverTool, searchTool];

const agentPrompt = await pull("hwchase17/openai-functions-agent");
const agentModel = new ChatOpenAI({
  model: "gpt-3.5-turbo-1106",
  temperature: 0,
});

const agent = await createOpenAIFunctionsAgent({
  llm: agentModel,
  tools,
  prompt: agentPrompt,
});

const agentExecutor = new AgentExecutor({
  agent,
  tools,
  verbose: true,
});

// Example 1
// const agentResult = await agentExecutor.invoke({
//   input: "how can LangSmith help with testing?",
// });

// console.log(agentResult.output);

// Example 2
// const agentResult = await agentExecutor.invoke({
//   input: "what is the weather in SF?",
// });

// console.log(agentResult.output);

// Conversation Example
const agentResult3 = await agentExecutor.invoke({
  chat_history: [
    new HumanMessage("Can LangSmith help test my LLM applications?"),
    new AIMessage("Yes!"),
  ],
  input: "Tell me how",
});

console.log(agentResult3.output);
