from peft import AutoPeftModelForCausalLM
from transformers import GenerationConfig
from transformers import AutoTokenizer
import torch
import streamlit as st
from streamlit_chat import message

st.session_state.clicked=True

def process_data_sample(example):

    # processed_example = "<|system|>\n You are a support chatbot who helps with user queries chatbot who always responds in the style of a professional.</s>\n<|user|>\n" + example + "</s>\n<|Debater|>\n"
    processed_example = "<|system|>\n You are a Debateable AI chatbot who engages in debates on the topic of the destruction of temples in India. As an unbiased and professional AI, you have your own views and opinions, and you strongly stand against the destruction of temples. You are ready to debate with anyone and present your points with conviction and evidence to support your stance.</s>\n<|user|>\n" + example + "</s>\n<|Debater|>\n" 
    return processed_example

@st.cache_resource(show_spinner=True)
def create_bot():

    tokenizer = AutoTokenizer.from_pretrained("Debate-AI")

    model = AutoPeftModelForCausalLM.from_pretrained(
                                                        "Debate-AI",
                                                        low_cpu_mem_usage=True,
                                                        return_dict=True,
                                                        torch_dtype=torch.float16,
                                                        device_map="cuda"
                                                    )

    generation_config = GenerationConfig(
                                            do_sample=True,
                                            temperature=0.5,
                                            max_new_tokens=256,
                                            pad_token_id=tokenizer.eos_token_id
                                        )
    
    return model, tokenizer, generation_config

model, tokenizer, generation_config = create_bot()

bot = create_bot()

def infer_bot(prompt):
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    outputs = model.generate(**inputs, generation_config=generation_config)
    out_str = tokenizer.decode(outputs[0], skip_special_tokens=True).replace(prompt, '')
    return out_str

def display_conversation(history):
    for i in range(len(history["Debater"])):
        message(history["user"][i], is_user=True, key=str(i) + "_user")
        message(history["Debater"][i],key=str(i))

def main():

  
    st.subheader("A Debatale chatbot created using Zephyr which was finetuned to possess the capabilities to be a Debater.")

    user_input = st.text_input("Enter your topic Related Temples Destruction.")

    if "Debater" not in st.session_state:
        st.session_state["Debater"] = ["I am ready to Have a debate with you on Hindu temples"]
    if "user" not in st.session_state:
        st.session_state["user"] = ["Hey there!"]
                
    if st.session_state.clicked:
        if st.button("Debate"):

            answer = infer_bot(user_input)
            st.session_state["user"].append(user_input)
            st.session_state["Debater"].append(answer)

            if st.session_state["Debater"]:
                display_conversation(st.session_state)

if __name__ == "__main__":
    main()