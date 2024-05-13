{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "38f8efdb-91d4-4e45-a5f8-2d75d212a2e1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Python script to scrape an article given the url of the article and store the extracted text in a file\n",
    "# Url: https://medium.com/@subashgandyer/papa-what-is-a-neural-network-c5e5cc427c7\n",
    "\n",
    "import os\n",
    "import requests\n",
    "import re\n",
    "# Code here - Import BeautifulSoup library\n",
    "from bs4 import BeautifulSoup  # Importing BeautifulSoup library\n",
    "\n",
    "\n",
    "# Code ends here\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "id": "8d0c1008-c716-4d1b-b7ff-173484443944",
   "metadata": {},
   "outputs": [],
   "source": [
    "# function to get the html source text of the medium article\n",
    "headers = {\n",
    "        \"User-Agent\" : \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36\"\n",
    "}\n",
    "\n",
    "def get_page():\n",
    "\tglobal url\n",
    "\t\n",
    "\t# Code here - Ask the user to input \"Enter url of a medium article: \" and collect it in url\n",
    "\turl = input(\"Enter url of a medium article: \")  # Ask the user to input \"Enter url of a medium article: \" and collect it in url\n",
    "\t# Code ends here\n",
    "\t\n",
    "\t# handling possible error\n",
    "\tif not re.match(r'https?://medium.com/',url):\n",
    "\t\tprint('Please enter a valid website, or make sure it is a medium article')\n",
    "\t\tsys.exit(1)\n",
    "\n",
    "   \n",
    "\n",
    "    \n",
    "\n",
    "\t# Code here - Call get method in requests object, pass url and collect it in res\n",
    "\tres = requests.get(url, headers=headers)  # Call get method in requests object, pass url and collect it in res\n",
    "\t# Code ends here\n",
    "\n",
    "\tres.raise_for_status()\n",
    "\tsoup = BeautifulSoup(res.text, 'html.parser')\n",
    "\treturn soup\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "ff7bbea6-d844-4b24-9822-11d0a88d39a2",
   "metadata": {},
   "outputs": [],
   "source": [
    "# function to remove all the html tags and replace some with specific strings\n",
    "def clean(text):\n",
    "    rep = {\"<br>\": \"\\n\", \"<br/>\": \"\\n\", \"<li>\":  \"\\n\"}\n",
    "    rep = dict((re.escape(k), v) for k, v in rep.items()) \n",
    "    pattern = re.compile(\"|\".join(rep.keys()))\n",
    "    text = pattern.sub(lambda m: rep[re.escape(m.group(0))], text)\n",
    "    text = re.sub(r'\\<(.*?)\\>', '', text)\n",
    "    return text\n",
    "\n",
    "\n",
    "def collect_text(soup):\n",
    "\ttext = f'url: {url}\\n\\n'\n",
    "\tpara_text = soup.find_all('p')\n",
    "\tprint(f\"paragraphs text = \\n {para_text}\")\n",
    "\tfor para in para_text:\n",
    "\t\ttext += f\"{para.text}\\n\\n\"\n",
    "\treturn text\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "6bc3b3c1-bef6-4ea4-9b15-5b2396cfeb7e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# function to save file in the current directory\n",
    "def save_file(text):\n",
    "    if not os.path.exists('./scraped_articles'):\n",
    "        os.mkdir('./scraped_articles')\n",
    "    name = url.split(\"/\")[-1]\n",
    "    print(name)\n",
    "    fname = f'scraped_articles/{name}.txt'\n",
    "\n",
    "    # Code here - write a file using with (2 lines)\n",
    "    with open(fname, 'w', encoding='utf-8') as file:\n",
    "        file.write(text)\n",
    "\n",
    "    # Code ends here\n",
    "\n",
    "    print(f'File saved in directory {fname}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "id": "65bf9d13-f920-427f-83f0-1992fecfc4e9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter url of a medium article:  https://medium.com/@subashgandyer/papa-what-is-a-neural-network-c5e5cc427c7\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "paragraphs text = \n",
      " [<p class=\"be b dw dx dy dz ea eb ec ed ee ef dt\"><span><button class=\"be b dw dx eg dy dz eh ea eb ei ej ed ek el ef em eo ep eq er es et eu ev ew ex ey ez fa fb fc bl fd fe\" data-testid=\"headerSignUpButton\">Sign up</button></span></p>, <p class=\"be b dw dx dy dz ea eb ec ed ee ef dt\"><span><a class=\"af ag ah ai aj ak al am an ao ap aq ar as at\" data-testid=\"headerSignInButton\" href=\"/m/signin?operation=login&amp;redirect=https%3A%2F%2Fmedium.com%2F%40subashgandyer%2Fpapa-what-is-a-neural-network-c5e5cc427c7&amp;source=post_page---two_column_layout_nav-----------------------global_nav-----------\" rel=\"noopener follow\">Sign in</a></span></p>, <p class=\"be b dw dx dy dz ea eb ec ed ee ef dt\"><span><button class=\"be b dw dx eg dy dz eh ea eb ei ej ed ek el ef em eo ep eq er es et eu ev ew ex ey ez fa fb fc bl fd fe\" data-testid=\"headerSignUpButton\">Sign up</button></span></p>, <p class=\"be b dw dx dy dz ea eb ec ed ee ef dt\"><span><a class=\"af ag ah ai aj ak al am an ao ap aq ar as at\" data-testid=\"headerSignInButton\" href=\"/m/signin?operation=login&amp;redirect=https%3A%2F%2Fmedium.com%2F%40subashgandyer%2Fpapa-what-is-a-neural-network-c5e5cc427c7&amp;source=post_page---two_column_layout_nav-----------------------global_nav-----------\" rel=\"noopener follow\">Sign in</a></span></p>, <p class=\"be b in io bj\"><a class=\"af ag ah ai aj ak al am an ao ap aq ar ip\" data-testid=\"authorName\" href=\"/@subashgandyer?source=post_page-----c5e5cc427c7--------------------------------\" rel=\"noopener follow\">Subash Gandyer</a></p>, <p class=\"be b in io dt\"><span><a class=\"is it ah ai aj ak al am an ao ap aq ar ew iu iv\" href=\"/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F28366f5ebce1&amp;operation=register&amp;redirect=https%3A%2F%2Fmedium.com%2F%40subashgandyer%2Fpapa-what-is-a-neural-network-c5e5cc427c7&amp;user=Subash+Gandyer&amp;userId=28366f5ebce1&amp;source=post_page-28366f5ebce1----c5e5cc427c7---------------------post_header-----------\" rel=\"noopener follow\">Follow</a></span></p>, <p class=\"be b du z dt\"><span class=\"ld\">--</span></p>, <p class=\"be b du z dt\"><span class=\"pw-responses-count le lf\">1</span></p>, <p class=\"be b bf z dt\">Listen</p>, <p class=\"be b bf z dt\">Share</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"7022\">It was a cozy Sunday afternoon in the month of February 2018. I just finished my huge customary Sunday lunch spread with family and resting along. Everyone in the family was taking a quick nap for a pre-planned evening outing. Well not everyone, actually.</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"d273\">My 4-year-old angel came running to me, asked me to play with her for a while. As I was lazy and not in a position to move after the big spread, I evaded the chance to play with her by telling her “Papa’s got some work baby. Got to code some stuff.” I thought that would be the end of the conversation. No! It wasn’t. As my daughter was very inquisitive, she asked me “Papa, what stuff?” I said, “I need to code something for my work.” She didn’t leave. She again asked, “What is code something?” I wanted to end this conversation, as I was half past asleep. “Just some stuff baby. You wouldn’t understand. Way beyond your age.” Tanishi never takes NO for an answer. “Papa, tell me what stuff means and something means.” Cannot help evade a cute curious face, I said, “I am working on Neural Network.” Before I finish the statement, “Papa, What is a Meural Metark?” I gave up my stubbornness of avoiding her. With a smile, I said slowly, “Its Neu — ral Net — work”</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"cdc5\">She asked, “Papa, What is Meu-ral Met-ark?”</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"79e6\">At the back of my head, thoughts of me taking days to comprehend what a NN (short for Neural Network) is, how it would work, where it is used, how it is simulating our human brain’s inner workings were going through. It took me days and weeks to understand fully and how can I make a 4-year-old understand what a Neural Network is. I never thought about teaching a complex concept to a kid before. It was way beyond their age. It was not a mere color or a shape or a number to teach. This was going to be interesting and challenging. I saw an opportunity here as a teacher (teaching professional college adults) to simplify the complex problem to a simpler understandable concept for a kid who doesn’t know anything apart from ABC, 1 to 20, Colors and Shapes. WOW! This was mind-boggling. I gave a couple of lectures to make my adult students understand what a Neural Network is when I taught them a mini-Machine Learning course. I rolled up my sleeves. Took up the challenge. Sat down beside my kid with pencil, drawing sheet and my laptop.</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"f38f\">Thinking of ways of what would be the best way to start teaching her. One simple methodology: I thought of starting with an easy-to-follow definition.</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"49ee\"><em class=\"od\">“Neural Network is a collection (a network) of neurons whose job is to learn a new thing or a new place or a new process or a new concept.”</em></p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"829e\">It would be stupid on my part to start with a definition of Neural Network like how we used to teach adults in college. No, it’s not right for a kid. Then, I thought of a way to start with her favorite hobby of drawing and coloring objects. Gave her a paper, ask her to draw a circle. She did. She didn’t stop there. She drew a face inside the circle. She did with great pride and smile. I drew a circle below. Asked her to draw a dog out of it. She drew a face on the circle, and then she drew one big ellipse next to head. Beneath the ellipse, she drew four legs downwards. She said, “That’s the dog daddy.” I was super impressed as her daddy. I said, “Good Job!” and asked her, “Where’s the tail, baby?” She smiled and drew a tail. That’s it. There’s a dog.</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"30d4\">I knew she never learnt to draw a lion. I took this opportunity to make her learn a new thing. After all, neural network inside our brain helps us to learn new things in our life. I said, “Baby, we would learn how to draw a lion now.” She’s bustling with energy said “Yayyyy! Lion!” and made “Grrrrrrrrr!!!” I tested her by asking her to try drawing a lion. She stumbled. She never came across a lion before. I told her, there would be a circle face, ellipse body, four legs, a tail and so on. What I was actually doing here was teaching her neural network (brain) the features of a lion like exactly how Machine Learning Engineers would train the machine to learn new features. After telling her the features of a lion, asked her “Can you draw these for me?” She happily drew almost a similar figure to that of a dog she drew before.</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"936b\">I said, “Very good”. But they look similar right? Now, we need to know the difference between a dog and a lion. What’s the difference? Lion is big. Dog is small. One big difference is the mane (the beard) just like your papa has. A big beard is the main difference between a lion and a dog. Now I took the pencil and drew a beard in the face. I told her this is a lion. A dog will have features like face, body, legs, and tail. A lion will have features like face, body, legs, tail and a beard. She was little confused, rightly so.</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"fc45\">Tried a different approach to teach her with visuals. I spend some time in collecting pictures of dogs and lions from Google images. Printed it and showed her a set of dogs and then a set of lions. I asked her what these pictures look like to you? Was it a dog or a lion? She kept mixing the answers first. After rewarding her for correct classifications with nice adjectives and correcting her for wrong classifications, her detection accuracy improved a lot after sometime. She slowly got used to it. She got trained. Her neural network got aligned with classifying Dogs and Lions after some training. If you’ve noticed, this is how ML people make their machines learn through Reinforcement Learning. This was how I trained my daughter to classify dogs and lions. She was so happy that she learnt a new thing by doing her favorite pastime of drawing and coloring.</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"c543\">She was happy and there was the neural network functioning concept that still remained to be taught to her. I asked her “What happened now baby? Did you learn something new today? Do you know what is the difference between a lion and a dog?” She said, “Yes.” I said, “This is called Learning. You just learnt a new thing today. How you learnt it is because of Neural Network inside your brain.” Now, a neural network is a collection of neurons that keeps switching on and off based on things you see, feel, hear and think just like switching on light bulb at our home.</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"5ecd\">“Your brain is here inside our head. Your brain has billions of neurons inside. Every neuron has a purpose of seeing a feature. You can think of a feature as a simpler form of an object. For example, a face object can be seen by neurons as a circle (face) with two smaller circles (two eyes), a line (nose) and a curved line (mouth). These are features in a face object. Neurons will look for these patterns (circle, line, curved line, smaller circles and so on). Every neuron is waiting for your eyes to see something new, for your nose to smell something new, for your ears to hear something new, for your tongue to taste something new. When something new is heard, or smelled, or seen, or tasted, the neurons will group together to send signals and forms connections with already seen, heard, tasted or smelled neurons. This is what is called as ‘Forming Logical Connections’ with the past. Once it is established, your brain will say, ‘Hey, this is dog. This is lion and so on.’ Every neuron would’ve seen, or heard, or smelled, or tasted certain features. When you see a new object, your brain will ask the neurons, ‘Hey, anybody experienced this before?’ The neurons will say, ‘Yes, I have seen this.’ Certain other neurons will say, ‘No, I have not seen this.’ The neurons that have seen this before, will group together and form logical connections from the past and gives us an object from our memory. For example, when I showed you a lion picture, your brain asked the neurons who had seen it before. The neurons grouped together with features like face, body, legs, tail and a beard forms a lion. Your brain looks for these features. Once all the features are there, the neurons will send a signal that the picture you are looking at is a lion and not a dog. This is what happens inside your brain, darling. This is also how all our learning happens.”</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"998b\">“In short, brain consists of billions of neurons. Every neuron will tune itself to pick up certain features like legs, tail, face, beard, and so on. When a picture is shown to you, your neurons will group together and tries to signal what that object is by forming logical connections between the past and the present. Ultimately, the neurons in your brain tell that it is a lion and not a dog. This is how your brain identifies things. This complex working of the neurons inside the brain works super fast in the order of milliseconds (very fast). In a few milliseconds, your brain identifies whether the picture is a lion or a dog. This is what a neural network is and this is how it works in identifying things. The same principle is applied for a song that you hear, a cartoon that you watch, a rhyme that you sing, an animal that you draw, a food that you taste, a flower that you smell and so on. Neurons work together in finding patterns and once a pattern is identified, it signals the brain that it is a thing, place, song, taste, smell and so on.”</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"97b5\">It was the time to test her understanding. I asked her simple questions to reiterate what she learnt just now. “Do you understand now, baby? Shall I ask you some questions? If you answer it correctly, I will take you out to the ice-cream parlor and you can have how much ever you want. “ The conversation went like this.</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"d25d\">Me: Where is your brain?</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"2409\">Tanishi: Its here (showing her head)</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"f15d\">Me: Correct! Where are the neurons located?</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"a07d\">Tanishi: Here (showing her head)</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"2522\">Me: Good! Who is responsible for identifying things, objects inside our brain?</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"4e2c\">Tanishi: Hmmmm. Don’t know.</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"43ee\">Me: I will give a clue. It starts with ’N’ and ends with a rhyming sound of ‘ons’</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"eac0\">Tanishi: Neurons</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"fe95\">Me: Good job, baby. Every neuron looks for something. What is a neuron looking for? I will give you a hint. Is it features?</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"009b\">Tanishi: Yes.</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"eb01\">Me: Tell me what neurons are looking for?</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"b74a\">Tanishi: Features.</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"f474\">Me: Great! When I ask you to draw a dog, what are the features there?</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"8d2e\">Tanishi: Help me. I don’t know.</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"243f\">Me: Okay, when I ask you to draw a dog, what is the first thing you draw?</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"f198\">Tanishi: Circle.</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"ce3a\">Me: Good. Circle represents what?</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"ef37\">Tanishi: Face</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"5689\">Me: Yeah, baby. Then what you draw next?</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"059c\">Tanishi: I draw eyes, nose, and mouth.</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"1b01\">Me: Good. That’s right. So, the face has got eyes, nose and mouth as features. Now tell me, what are the features in a face?</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"1348\">Tanishi: Eyes, nose, mouth</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"a0e3\">Me: Brilliant! After the face, what do you draw for completing a dog?</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"4ee2\">Tanishi: Body</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"7fd8\">Me: What shape is the body?</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"1b0d\">Tanishi: Ellipse</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"8a41\">Me: Nice. This is also a feature that our neurons are looking for. What’s next?</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"ed6e\">Tanishi: Legs</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"e1c4\">Me: How many legs does a dog have?</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"15f4\">Tanishi: 1,2,3,4. 4 legs</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"d09c\">Me: Good. Anything else to draw in a dog?</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"b8dd\">Tanishi: That’s it.</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"16bf\">Me: Hey how about a tail? Dogs have tail?</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"fc5e\">Tanishi: Yes.</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"51d2\">Me: So, for a dog, the features are face, body, legs and tail. Do you understand what are the features now for a dog?</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"0400\">Tanishi: Yes!!!</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"cd53\">Me: What are they?</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"40c9\">Tanishi: Face, body, legs and tail</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"4d40\">Me: Amazing baby. If I ask you to draw a lion, what are the features? Same features as a dog but with an extra feature. Can you tell me what that extra feature is for a lion? It starts with ‘B’</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"3685\">Tanishi: Beard. (Holding my beard, she smiled and said) Beard like you</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"3199\">Me: Yes, darling. Good job. So, neurons are inside our brain waiting for features. To identify an object, it looks for features. Once the features are seen and a logical connection is established, neurons signals your brain that it is a lion. Who sends signal to the brain?</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"e5a5\">Tanishi: Neurons</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"e8b1\">Me: Now, these neurons are working together as friends. They are like your friends Daisy, Rose, Isabelle and Hayami. All neurons work together like your friends and identify lion and dog. So, this group of neuron friends is called as Neural Network. Tell me, what is a neural network?</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"749a\">Tanishi: Neuron friends</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"66c5\">Me: Good. Neural network is a group of neuron friends identifying lions and dogs. Do you understand Neural Network now?</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"619e\">Tanishi: Yes papa.</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"9ddc\">Me: Brilliant job baby. Come, let’s go, and get some ice creams for my lovely angel.</p>, <p class=\"pw-post-body-paragraph ml mm gt mn b mo mp mq mr ms mt mu mv mw mx my mz na nb nc nd ne nf ng nh ni gm bj\" id=\"915a\">Phew! That was a challenging and a learning experience for me as well. That was how I ended my Sunday afternoon with my brilliant daughter who can teach other kids what a Meural Metark is. And I hope she will not come to me running asking “Papa, what is Meural Metark?” again. And I have a strong feeling; she would ask me another stunning question sooner or later. Fingers crossed and I am prepared to take up the challenges coming my way in the future.</p>, <p class=\"be b du z dt\"><span class=\"ld\">--</span></p>, <p class=\"be b du z dt\"><span class=\"ld\">--</span></p>, <p class=\"be b bf z dt\"><span class=\"pw-responses-count le lf\">1</span></p>, <p class=\"be b bf z bj\"><span class=\"gm\">CS Teacher to ...</span></p>, <p class=\"be b du z dt\">Help</p>, <p class=\"be b du z dt\">Status</p>, <p class=\"be b du z dt\">About</p>, <p class=\"be b du z dt\">Careers</p>, <p class=\"be b du z dt\">Blog</p>, <p class=\"be b du z dt\">Privacy</p>, <p class=\"be b du z dt\">Terms</p>, <p class=\"be b du z dt\">Text to speech</p>, <p class=\"be b du z dt\">Teams</p>]\n",
      "papa-what-is-a-neural-network-c5e5cc427c7\n",
      "File saved in directory scraped_articles/papa-what-is-a-neural-network-c5e5cc427c7.txt\n"
     ]
    }
   ],
   "source": [
    "if __name__ == '__main__':\n",
    "\ttext = collect_text(get_page())\n",
    "\tsave_file(text)\n",
    "\t# Instructions to Run this python code\n",
    "\t# Give url as https://medium.com/@subashgandyer/papa-what-is-a-neural-network-c5e5cc427c7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "58a71237-0980-47be-9c0a-f8b29de3fa16",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
