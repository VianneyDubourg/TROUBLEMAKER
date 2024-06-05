# Trouble Maker: A Truth or Dare generator based on Markov Chain

By Vianney Dubourg and Valentin Baron. 
Inspired by Yuqing Liang and Yibo Fu.

### Introduction

Trouble Maker is a game gadget designed to address the common pain point of running out of prompts in various games, especially Truth or Dare. It utilizes Markov Chain to generate random prompts, offering a solution to the challenge of continuously devising clever prompts yourself. The prompts available online are often limited and repetitive, making it difficult to keep the game engaging over time. With Trouble Maker, players can enjoy an endless array of fresh and entertaining prompts, enhancing the overall experience of the game.

We introduce a novel method for generating prompts using Markovify, a straightforward machine learning generator based on Markov Chains. Markovify predicts the next word based on the preceding word rather than the entire sentence. This limitation, where the model doesn't grasp the true meaning of each sentence, leads to the absurdity of the prompts and enhances their unpredictability. By incorporating a diverse range of inputs, from absurd to serious content, Markovify can create an endless array of challenges for players that stretch beyond human imagination.

### Why Markov Chain? 

A Markov chain is a stochastic model that generates random results based on probability. In text generation, a Markov chain model predicts the next word based on the previous word. Unlike pre-trained text generation models like GPT-3, Markov Chain models have a very limited understanding of the input text, resulting in outputs that often make less sense. This inherent absurdity makes primitive ML applications a perfect match for the playful nature of the Truth or Dare game – demonstrating that "errors" in machine learning can be entertaining when used appropriately.

Furthermore, pre-trained ML models are complex and resource-intensive, requiring significant computational power and advanced hardware. They also take longer to train and execute, which is impractical for a game tool. Despite their sophistication, these models still produce unpredictable results.

Markovify, being a simpler and lighter model, is more environmentally friendly and user-friendly. For the straightforward task of generating Truth or Dare prompts, Markovify is a superior choice due to its efficiency and ease of use.


### Why a Gadget? 

We propose a small, hand-sized gadget equipped with a built-in thermal printer for generating each prompt. While there are numerous web-based or app-based tools for Truth or Dare and other party games, these screen-based tools often detract from the fun. They tend to divert players' attention to the electronic device, which can be disruptive due to incoming messages and notifications. A party game should foster real-life connections, whereas electronic devices typically do the opposite.

Our gadget aims to offer a break from the overuse of electronics. By providing prompts printed on slips of paper, this device ensures that players remain fully engaged with the present moment and, more importantly, with each other.

### Selected input and testing

We used Markovify, a simple and extensible Markov chain generator, to produce sentences based on user input. For example, if the input is "Alice in Wonderland," the output might be something like, “Alice thought she might as well look and see what was the matter with it,” which sounds like a quote from the book but is actually generated. To create Dares, we input instructive sentences or phrases. Initially, we tested with 260 Dare prompts collected from websites. The results were promising, but the limited input size led to the model merely reorganizing the input according to natural language rules.

Since available Dares online are limited, we expanded our input to other instructive sources to create more varied and absurd outputs. This approach not only increased the absurdity of the prompts but also enhanced the machine’s creativity.

We categorized inputs for specific scenarios. For instance, a randomly generated cocktail recipe from a list of recipes can be used in a bar, prompting players to order "adventurous drinks" based on the generated recipe. Similarly, a nonsensical workout instruction can serve as a humorous challenge in the game.

After extensive testing with various combined inputs, we selected eight input sources divided into five categories:

  1- Truth or Dare: Generated from truth and dare prompts collected from the internet.
  2- Rap quotes: Selected on the Internet with ChatGPT.
  3- Famous quotes: Selected on the Internet with ChatGPT.
  4- Random text: Selected on the Internet with ChatGPT.
  5- Dinosaur's names/descriptions: Selected on the Internet with ChatGPT.

By using Markovify with these diverse and categorized inputs, we crafted a range of creative and entertaining prompts for various game scenarios.

### “Fine tuning”

Due to the unpredictable nature of machine learning and the 'immature' generating principle of our model, the generated output prompts often do not make complete sense to humans. The success rate for producing understandable sentences is below 50% without further modifications. Therefore, we implemented a series of "fine-tuning" procedures to enhance the quality of the output by adding constraints to minimize nonsensical or erroneous sentences.

We modified the Python script to clean up the input text, removing unnecessary symbols and spaces specific to each input type. For example, truth inputs often come with numbered bullets, and cocktail recipes contain many “\n” and “\r” codes within the text.

Despite these adjustments, we cannot guarantee that 100% of the generated prompts will be understandable, even after fine-tuning. Additionally, with a large enough input, the results can vary widely, and it’s difficult to predict if the same prompt will be generated again. Consequently, there should be a fault tolerance rate of 10-26%, depending on the input categories.

### Generated results Showcase

From our analysis, it's evident that the Truth or Dare challenges, dinosaur names, and rap quotes yield particularly successful results. Markovify effectively transforms serious input into absurd prompts in these categories.

For traditional dares generated from collected prompts online, the machine attempts to reorganize the limited input to generate new sentences, albeit with varying degrees of success.

We've gathered some intriguing results from all five categories, showcasing the diversity and creativity of the generated prompts.

#### Different games:
  
  Truth or Dare
  
  Rap quotes
  
  Famous quotes
  
  Random text
  
  Dinosaur's name
  
  Dinosaur's description


