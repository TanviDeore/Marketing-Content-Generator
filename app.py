import streamlit as st
import ollama 
import time

def generated_output(data,product_data,role):
    generated_data = ""

    progress_bar = st.progress(0)
    status = st.empty()
    for i in range(40):
        time.sleep(0.02)
        progress_bar.progress(i + 1)
        status.text("Generating product description...")

    try:
        if(data == 1):  prompt_desc = create_product_description_prompt(product_data)
        else: prompt_desc = create_ad_copy_prompt(product_data)
        response_desc = ollama.chat(
            model='gemma',
            messages=[
            {'role': 'system', 'content': role},
            {'role': 'user', 'content': prompt_desc}
            ],
            options={'temperature': 0.7, 'num_predict': 300}
        )
        generated_data = response_desc['message']['content'].strip()
        progress_bar.progress(100)
        status.text("Product output generated.")
    except Exception as e:
        st.error(f"Error generating description: {e}")
        generated_data = "Could not generate output."
        progress_bar.empty()
    finally: return generated_data

def create_product_description_prompt(product_data):
    
    features_str = ", ".join(product_data['Key Features'])
    benefits_str = ", ".join(product_data['Key Benefits'])

    
    target_audience_str = product_data['Target Audience']
    desired_tone_str = product_data['Desired Tone']

    prompt = f"""
    You are a highly skilled marketing copywriter for e-commerce products.
    Your task is to generate a compelling and personalized product description.
    Do not invent facts or features. Only use provided information.
    Start directly with the product description without any introduction like "here is compelling description.." etc.
    IMPORTANT: Ensure the language used is inclusive and avoids assuming specific dominant demographics or characteristics as defaults (e.g., right-handed, left-handed, gender, etc. is not included). Describe features factually.
    Do not include terms like right-handed, left-handed, demographic details, or gender-specific pronouns if not explicitly necessary for the product.

    Here is the product information:
    Product Name: {product_data['Product Name']}
    Category: {product_data['Product Category']}
    Key Features: {features_str}
    Key Benefits: {benefits_str}
    Target Audience: {target_audience_str}
    Desired Tone: {desired_tone_str}

    Please generate a product description that is between 100-200 words.
    The description should be engaging, highlight the benefits relevant to the target audience,
    and be written in a {desired_tone_str} tone.
    Ensure it persuades the specified target audience.
    """
    return prompt

def create_ad_copy_prompt(product_data):
    
    features_str = ", ".join(product_data['Key Features'])
    benefits_str = ", ".join(product_data['Key Benefits'])

    
    target_audience_str = product_data['Target Audience']
    desired_tone_str = product_data['Desired Tone']

    prompt = f"""
    You are a highly skilled advertisement copywriter for e-commerce products.
    Your task is to generate a compelling and personalized Advertisement.
    Do not invent facts or features. Only use provided information.
    Start directly with the product advertisement without any introduction like "here is compelling advertisement.." etc.
    IMPORTANT: Ensure the language used is inclusive and avoids assuming specific dominant demographics or characteristics as defaults (e.g., right-handed, left-handed, gender, etc. is not included). Mention features factually.
    Do not include terms like right-handed, left-handed, demographic details, or gender-specific pronouns if not explicitly necessary for the product.
    
    Here is the product information:
    Product Name: {product_data['Product Name']}
    Key Features: {features_str}
    Key Benefits: {benefits_str}
    Target Audience: {target_audience_str}
    Desired Tone: {desired_tone_str}

    Generate 3 distinct, catchy, crisp headlines for the Advertisement. Use punchy and concise language. Each headline should be under 6 words.
    Mention the headline of Advertisement as #Headline1, #Headline2, #Headline3 in separate lines. Each headline should focus on a distinct feature or benefit that attracts the target audience most.

    Following the headlines, generate 1-2 lines of short body text for the advertisement, under 80 words total, placed directly below the headlines. Make sure to not include "body lines" anywhere in the generated text.
    Make sure advertisement body lines or headlines are not a direct copy of the product description.
    The Advertisement should be engaging, highlight the benefits relevant to the target audience, and be written in a {desired_tone_str} tone.
    Ensure it persuades the specified target audience.
    IMPORTANT: Do not use body text, benethe headlines while generating body text, directly start with the text generation
    """
    return prompt

#Streamlit App Layout

st.title("Product Marketing Content Generator")
st.markdown("Generate compelling product descriptions and ad copy.")

# Input Fields
with st.form("product_input_form"):
    st.subheader("Product Details")
    product_name = st.text_input("Product Name", "")
    product_category = st.text_input("Product Category","")
    key_features_input = st.text_area("Key Features (comma-separated)", "")
    key_benefits_input = st.text_area("Key Benefits (comma-separated)", "")
    target_audience = st.text_input("Target Audience", "")
    desired_tone = st.text_input("Desired Tone", "")

    submitted = st.form_submit_button("Generate Content")
    

# 
if submitted:
    # Preparing product_data dictionary from Streamlit inputs
    product_data = {
        "Product Name": product_name,
        "Product Category": product_category,
        "Key Features": key_features_input,
        "Key Benefits": key_benefits_input,
        "Target Audience": target_audience,
        "Desired Tone": desired_tone
    }
    missing_fields = [label for label, value in product_data.items() if not value.strip()] 

    if missing_fields:
        st.error(f"Please fill in all the required fields: {', '.join(missing_fields)}")
    else:
        role1 = 'You are an expert e-commerce marketing copywriter. Generate only the product description. Do NOT include any introductory phrases or preambles.'
        role2 = 'You are an expert advertisement copywriter. Generate only the ad copy. Do NOT include any introductory phrases or preambles.'
        generated_description = generated_output(1,product_data,role1)
        generated_ad_copy = generated_output(0,product_data,role2)
    
    # Displaying Output
        st.subheader("Generated Product Description")
        st.markdown(generated_description) 

        st.subheader("Generated Ad Copy")
        st.markdown(generated_ad_copy) 

        st.success("Content generation complete!")
