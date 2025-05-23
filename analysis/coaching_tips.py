from transformers import pipeline
model_name = "MBZUAI/LaMini-Flan-T5-783M"

generator = pipeline("text2text-generation", model=model_name)



def generate_tips(transcript, sentiment, pacing, filler_count):
    prompt = (
        "You are a friendly but insightful public speaking coach.\n"
        "Even if the speaker performs well, you always give 3 tips — either for improvement or for reinforcing good habits.\n\n"
        f"Speech analysis:\n"
        f"- Sentiment: {sentiment}\n"
        f"- Pacing score: {pacing:.2f}\n"
        f"- Filler words: {filler_count}\n"
        f"- Transcript: \"{transcript[:120]}...\"\n\n"
        "Write 3 specific tips to help this speaker improve or maintain their public speaking quality."
    )




    result = generator(
        prompt,
        max_length=100,
        temperature=0.9,
        top_p=0.9,
        repetition_penalty=1.8,
        do_sample=True
    )

    return result[0]["generated_text"].strip()
