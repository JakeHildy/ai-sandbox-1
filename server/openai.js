import OpenAI from "openai";
import dotenv from "dotenv";
import { getFruits } from "./externalApi.js";

dotenv.config();
const GPT_MODEL = "gpt-3.5-turbo";

const openai = new OpenAI({
  organization: process.env.OPENAI_ORGANIZATION,
  apiKey: process.env.OPENAI_API_KEY,
});

const isFunctionCall = (response) => {
  if (response.choices[0].finish_reason === "tool_calls") {
    const name = response.choices[0].message.tool_calls[0].function.name;
    const args = response.choices[0].message.tool_calls[0].function.arguments;
    return { name, args };
  }
  return null;
};

export const chatCompletionRequest = async (
  messages,
  tools = null,
  toolChoice = null,
  model = GPT_MODEL
) => {
  try {
    return await openai.chat.completions.create({
      model,
      messages,
      tools,
      tool_choice: toolChoice,
    });
  } catch (err) {
    console.log(err);
  }
};

export const openAI = {
  async generateText(prompt) {
    const messages = [
      {
        role: "system",
        content:
          "You are a very helpful assistant that will figure out the best way to help the user.",
      },
      { role: "user", content: prompt },
    ];

    const tools = [
      {
        type: "function",
        function: {
          name: "get_fruits",
          description:
            "Get a list of fruits. Returns an array of fruits that contains their name, weight, category and price.",
          // parameters: {
          //   type: "object",
          //   properties: {
          //     location: {
          //       type: "string",
          //       description: "The city and state, e.g. San Francisco, CA",
          //     },
          //     unit: { type: "string", enum: ["celsius", "fahrenheit"] },
          //   },
          //   required: ["location"],
          // },
        },
      },
    ];

    let response;
    try {
      response = await openai.chat.completions.create({
        model: "gpt-3.5-turbo", // or any other model you prefer
        messages,
        tools,
        tool_choice: "auto",
      });

      if (isFunctionCall(response)) {
        const { name, args } = isFunctionCall(response);

        if (name === "get_fruits") {
          const fruits = await getFruits();
          messages.unshift({
            role: "user",
            content: `Here are the fruits: ${JSON.stringify(fruits)}`,
          });
        }

        response = await openai.chat.completions.create({
          model: "gpt-3.5-turbo", // or any other model you prefer
          messages,
        });
      }
    } catch (error) {
      console.error("OpenAI API error:", error);
      throw error;
    }
    console.log(response.choices[0].message.content);
    return response.choices[0].message.content;
  },
};
