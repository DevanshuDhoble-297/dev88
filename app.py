import streamlit  as st
import os
import google.generativeai as genai
from api_key import google_gemini_api_key,openai_api_key
from openai import OpenAI
client = OpenAI(api_key=openai_api_key)
genai.configure(api_key=google_gemini_api_key)
generation_config = {
  "temperature": 1.05,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
)


st.set_page_config(layout="wide") 
#tittle 
st.title('Blogcraft: Your AI write comapnion')
  #sub header
st.subheader("Now you can craft perfect blogs ")

with st.sidebar:
    st.title("input your blog details")
    st.subheader("enter details of the blog") 
    #blog title
    blog_title=st.text_input("blog Title")
    #keywords input
    keywords=st.text_area("Keywords(comma.separated)")
    num_words=st.slider("number of words",min_value=250,max_value=1000,step=100)
    num_images=st.number_input("Number of images",min_value=1,max_value=5,step=1)
    submit_button=st.button("genrate blog")
    chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "genrate a blog on effects of ai with title and with informative things and words limt 150 ",
      ],
    },
    {
      "role": "model",
      "parts": [
        "## AI's Ripple Effect: Transforming Our World\n\nArtificial intelligence (AI) is rapidly reshaping our lives, impacting everything from healthcare and finance to entertainment and transportation.  AI-powered diagnostics improve medical accuracy, while algorithms personalize our online experiences.  Automation streamlines industries, increasing efficiency but also raising concerns about job displacement.  Furthermore, AI's influence on decision-making processes raises ethical questions about bias and transparency.  While the full impact remains to be seen, AI's transformative power is undeniable, demanding careful consideration of its potential benefits and challenges as we navigate this evolving landscape.\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "enrate a blog on effects of ai with title and with informative things and words limt 500",
      ],
    },
    {
      "role": "model",
      "parts": [
        "## The Two Sides of the Coin: Exploring the Profound Effects of AI\n\nArtificial intelligence (AI) is no longer a futuristic fantasy; it's woven into the fabric of our daily lives, transforming industries and reshaping the way we interact with the world.  From the mundane to the groundbreaking, AI's influence is undeniable, presenting both remarkable opportunities and complex challenges.\n\n**The Bright Side: AI's Transformative Potential**\n\nAI's potential to revolutionize various sectors is immense. In healthcare, AI-powered diagnostic tools are enhancing accuracy and speed, leading to earlier disease detection and personalized treatment plans.  Drug discovery is being accelerated through AI algorithms that can analyze vast datasets and identify promising candidates.  In finance, AI is streamlining processes, detecting fraud, and providing personalized financial advice.\n\nBeyond these specific sectors, AI is enhancing our everyday experiences.  Smart assistants anticipate our needs, personalized recommendations guide our choices, and autonomous vehicles promise safer and more efficient transportation.  AI-powered language translation breaks down communication barriers, connecting people across the globe. The potential for increased productivity, personalized experiences, and scientific breakthroughs is truly remarkable.\n\n**The Dark Side: Navigating the Challenges of AI**\n\nDespite its transformative potential, AI also presents significant challenges. Job displacement due to automation is a growing concern, particularly in sectors heavily reliant on repetitive tasks.  The need for reskilling and upskilling the workforce to adapt to the changing job market becomes paramount.\n\nEthical considerations surrounding AI are equally complex.  Bias in algorithms can perpetuate and amplify existing societal inequalities.  The lack of transparency in some AI systems raises concerns about accountability and fairness in decision-making processes.  The potential for misuse of AI in areas like surveillance and autonomous weapons systems necessitates careful regulation and ethical frameworks.\n\nFurthermore, the increasing reliance on AI raises questions about data privacy and security.  As AI systems collect and analyze vast amounts of personal data, ensuring the responsible handling and protection of this information is crucial.\n\n**The Path Forward: Embracing Responsible AI Development**\n\nThe future of AI hinges on our ability to harness its potential while mitigating its risks.  This requires a multi-faceted approach involving collaboration between researchers, policymakers, and the public.  Promoting ethical AI development through transparency, fairness, and accountability is crucial.  Investing in education and training programs to prepare the workforce for the future of work is essential.  Establishing clear regulatory frameworks to govern the development and deployment of AI systems will be vital in ensuring its responsible and beneficial use.\n\nAI is a powerful tool, and like any tool, its impact depends on how we wield it. By embracing responsible AI development, fostering open dialogue, and prioritizing ethical considerations, we can navigate the complexities of this transformative technology and unlock its full potential for the betterment of humanity.\n",
      ],
    },
  ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)  
    


if submit_button:
   #   st.image("https://fastly.picsum.photos/id/1/200/300.jpg?hmac=jH5bDkLr6Tgy3oAg5khKCHeunZMHq0ehBZr6vGifPLY")
  #  response = chat_session.send_message("INSERT_INPUT_HERE")

    st.write(response.text)
      