import express from "express";
import cors from "cors";

const app = express();
const port = 4000;

// Middleware
app.use(cors());
app.use(express.json());

app.get("/v1/fruits", (req, res) => {
  const fruits = [
    { name: "Apple", weight: "200g", category: "Tree fruit", price: "$0.50" },
    { name: "Banana", weight: "120g", category: "Tropical", price: "$0.30" },
    { name: "Cherry", weight: "5g", category: "Berries", price: "$0.10" },
    { name: "Date", weight: "7g", category: "Tropical", price: "$0.20" },
    { name: "Elderberry", weight: "5g", category: "Berries", price: "$0.15" },
    { name: "Fig", weight: "40g", category: "Tree fruit", price: "$0.40" },
    { name: "Grape", weight: "5g", category: "Berries", price: "$0.05" },
    { name: "Honeydew", weight: "1.8kg", category: "Melons", price: "$3.00" },
    {
      name: "Italian Plum",
      weight: "80g",
      category: "Stone fruit",
      price: "$0.60",
    },
    {
      name: "Jackfruit",
      weight: "10kg",
      category: "Tropical",
      price: "$25.00",
    },
    { name: "Kiwi", weight: "75g", category: "Berries", price: "$0.40" },
    { name: "Lemon", weight: "100g", category: "Citrus", price: "$0.50" },
    { name: "Mango", weight: "200g", category: "Tropical", price: "$1.50" },
    {
      name: "Nectarine",
      weight: "150g",
      category: "Stone fruit",
      price: "$0.70",
    },
    { name: "Orange", weight: "130g", category: "Citrus", price: "$0.60" },
  ];
  res.json({ count: fruits.length, data: fruits });
});

app.get("/v1/animals", (req, res) => {
  const animals = [
    {
      name: "African Elephant",
      species: "Loxodonta africana",
      endangeredLevel: "Vulnerable",
      countryOfOrigin: "Sub-Saharan Africa",
      description:
        "The African Elephant is the largest land mammal, known for its large ears and tusks.",
    },
    {
      name: "Giant Panda",
      species: "Ailuropoda melanoleuca",
      endangeredLevel: "Vulnerable",
      countryOfOrigin: "China",
      description:
        "Giant Pandas are bear-like in shape with distinctive black and white coloring, known for their diet primarily consisting of bamboo.",
    },
    {
      name: "Tiger",
      species: "Panthera tigris",
      endangeredLevel: "Endangered",
      countryOfOrigin: "Asia",
      description:
        "Tigers are the largest cat species, recognizable by their dark vertical stripes on orange-brown fur.",
    },
    {
      name: "Blue Whale",
      species: "Balaenoptera musculus",
      endangeredLevel: "Endangered",
      countryOfOrigin: "Global Oceans",
      description:
        "The Blue Whale is the largest animal ever known to have existed, living in all the world's oceans except the Arctic.",
    },
    {
      name: "Orangutan",
      species: "Pongo abelii & Pongo pygmaeus",
      endangeredLevel: "Critically Endangered",
      countryOfOrigin: "Indonesia and Malaysia",
      description:
        "Orangutans are great apes known for their reddish-brown hair and strong arms.",
    },
    {
      name: "Snow Leopard",
      species: "Panthera uncia",
      endangeredLevel: "Vulnerable",
      countryOfOrigin: "Central and South Asia",
      description:
        "Snow Leopards are large cats adapted to the cold, mountainous environments of Central and South Asia.",
    },
    {
      name: "Mountain Gorilla",
      species: "Gorilla beringei beringei",
      endangeredLevel: "Endangered",
      countryOfOrigin: "Central Africa",
      description:
        "Mountain Gorillas are a subspecies of eastern gorilla, living in forested mountains and known for their strong family bonds.",
    },
    {
      name: "Sea Turtle",
      species: "Cheloniidae and Dermochelyidae",
      endangeredLevel: "Vulnerable to Critically Endangered",
      countryOfOrigin: "Global Oceans",
      description:
        "Sea Turtles are marine reptiles that have existed for over 100 million years, known for their long migrations between feeding and nesting grounds.",
    },
    {
      name: "Amur Leopard",
      species: "Panthera pardus orientalis",
      endangeredLevel: "Critically Endangered",
      countryOfOrigin: "Russia and China",
      description:
        "The Amur Leopard is one of the world's most endangered big cats, known for its beautiful spotted fur.",
    },
    {
      name: "African Wild Dog",
      species: "Lycaon pictus",
      endangeredLevel: "Endangered",
      countryOfOrigin: "Sub-Saharan Africa",
      description:
        "African Wild Dogs are highly social predators, known for their painted fur and large, rounded ears.",
    },
    {
      name: "Siberian Tiger",
      species: "Panthera tigris altaica",
      endangeredLevel: "Endangered",
      countryOfOrigin: "Russia",
      description:
        "The Siberian Tiger, also known as the Amur tiger, is the world's largest cat, adapted to the cold environment of its habitat.",
    },
    {
      name: "Saola",
      species: "Pseudoryx nghetinhensis",
      endangeredLevel: "Critically Endangered",
      countryOfOrigin: "Vietnam and Laos",
      description:
        "The Saola, also known as the Asian unicorn, is a rare and mysterious hoofed mammal, discovered only in 1992.",
    },
  ];
  res.json({ count: animals.length, data: animals });
});

// Server
app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});
