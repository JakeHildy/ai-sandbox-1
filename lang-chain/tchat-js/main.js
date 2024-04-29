import { config } from "dotenv";
import { ChatOpenAI } from "@langchain/openai";
import { ChatPromptTemplate } from "@langchain/core/prompts";
import { StringOutputParser } from "@langchain/core/output_parsers";

import boxen from "./boxen.js";
import rl from "./readline.js";

config();

const chatModel = new ChatOpenAI({});
const outputParser = new StringOutputParser();

const prompt = ChatPromptTemplate.fromMessages([
  [
    "system",
    "You are an expert on hockey history. Give results that include lots of stats. ",
  ],
  ["user", "{input}"],
]);

const chain = prompt.pipe(chatModel).pipe(outputParser);

const loop = () => {
  rl.question(">> ", async (content) => {
    const result = await chain.invoke({
      input: content,
    });
    boxen(result, "Open AI", "ai");
    loop();
  });
};

loop();
