# Trouble Maker: A Truth or Dare generator based on Markov Chain

By Vianney Dubourg and Valentin Baron. 

### Introduction

Trouble Maker is a game-gadget that **generates random prompts for different games using Markov Chain** espacially Truth or Dare game: **running out of prompts is a common pain point of the game**. It is challenging to continuously devise clever prompts yourself and the prompts you can find online are often limited and repetitive in content.

We propose an innovative way to generate prompts using Markovify — a simple machine learning generator based on Markov Chain. Markovify predicts the next word based upon its previous word, but not the whole sentence. **The fact that this machine learning model doesn't really understand the true meaning of each sentence results in the absurdity of the prompts, and makes it more unpredictable**. By using a series of selected inputs, including both absurd and serious content, Morkovify can generate 'infinite' challenges for the players that are beyond the human imagination.

### Why Markov Chain? 

A Markov chain is a stochastic model that generate random results based on probability. In the text generating process, a Markov chain model predicts the next word based on the previous word. Compared to pre-trained text generation models like GPT-3, Markov Chain models actually have a very poor understanding of the input text, which means the generated results make less sense. The absurdity of such primitive ML application and the absurdity of the Truth or Dare game itself are just perfect match - “errors” in machine learning can be fun when put into right place.  
Moreover, the pre-trained ML models are rather complex and heavy, meaning they’re computationally expensive and requires better machine. Heavier model also takes longer to train and run, which would be a nightmare for a game tool. And due to the unpredictable nature of machine learning, there will still be a lot of uncertainty for the result even with a smarter model. 
Markovify, as a lighter model, is environmentally friendly and easier to use. For a simple purpose as generating truth or dare prompts, Markovify is definitely a better choice. 


### Why a Gadget? 

We propose this small hand-size gadget with a built-in thermal printer for generating each prompt.
There are plenty of web based or app based tools for truths and dares, just like for many other party games. However, we realized that using these screen based tools can kill so much fun, since these tools often divert the players' attention to the electronic device, which can distract them from the party with incoming messages and other notifications. A party game is meant to bond people together in reality, while electronic devices does exactly the opposite.
We intend to create a gadget that provides a getaway from the excessive use of electronics lifestyle. With the prompts thermal printed on tips as the interface, the players can be fully concentrated on the reality and more importantly, on each other. 

### Selected input and testing

We used Markovify, a simple and extensible Markov chain generator. The generator can produce sentences based on the user input. For example, if the input is the book Alice in Wonderland, the generated result includes “Alice thought she might as well look and see what was the matter with it.” - reasonable to be considered as a quote from the book but in fact not. To generate Dares, the input needs to be instructive sentences or phrases. First we tested with 260 Dare prompts we collected from some websites - the result looks good, but as the input is quite small, we can clearly see that the model re-grouped the input based on natural language rules. As the Dares we can find online is limited, we started to look for other instructive inputs that can become dares after random combination. Besides, mixing seemingly unrelated input increases the absurdity of the output, and helps to boost the machine’s imagination.
Categorized input can be used in specific scenarios. For example, a random cocktail recipe generated from a list of cocktail recipes can be used when the players are in a bar, where they can order “adventurous drinks” made out of the generated recipe; a generated workout instruction that doesn’t make sense in terms of exercising can be a funny challenge to do for the game. 
After testing with a variety of combined input, we selected 8 input sources and put them into 5 categories. The **Truth** and **Traditional Dare**** are generated from truth and dare prompts we gathered from the internet. The **Dark Drinks** are generated from a cocktail recipe database (we extracted the instructive texts from this database, see our code here) and a list of seasonings and sauce. The **Anti-human Workout** is a combination of workout instructions and table manner instructions, which is the most challenging one among the five. Finally, the **Mime** Challenge is a combination of a list of mime ideas we collected from the internet, some meditation scripts, as well as workout instructions and the table manners - combining these four inputs results in surprisingly dramatic prompts. 

### “Fine tuning”

Due to the unpredictable nature of machine learning, its ‘immature’ generating principle and the purpose of our generated output prompts, the outputs do not all make sense to us(human beings). The success rate of an understandable human language sentence is lower than 50% without further modifications. Therefore we have to conduct a series of “fine tuning” procedures to the output by adding up constraints to avoid the nonsense or error sentences. 
We modified the Python script to clean up the input text by removing unnecessary symbols and spaces based on different input. For example, the truth input comes with numbered bullets, and the cocktail recipe has a lot of “\n” and “\r” codes within the text.  

However we still cannot guarantee that 100% of the generated prompts are understandable even after the fine tuning process. Also, as long as the input is big enough, we can’t tell whether we’ll get the same result again or not. So there should be a fault tolerance rate of 10-26% based on the different input categories. 

### Generated results Showcase

From the result, we can see that the mime challenge, anti-human workout and dark drinks are especially successful, as Markovify managed to convert the serious input into absurd prompts. The traditional dares are generated from collected dare prompts from the internet, we can see the machine is attempting to reorganize the limited input to generate new sentences. 
We collected some interesting results of all five categories.

#### Different games:
  
  Truth or Dare
  Rap quotes
  Famous quote
  Random text
  Dinosaur's name
  Dinosaur's description


