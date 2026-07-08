import os

from config import INPUT_DIR


def generate_sandbox():
    """Generates an unstructured, chaotic directory of messy text data."""
    if not os.path.exists(INPUT_DIR):
        os.makedirs(INPUT_DIR)
        print(f"[SETUP] Created intake directory: {INPUT_DIR}")

    # File 1: A raw, poorly spelled support email
    email_content = """
    RE: URGENT COMPLAINT!!
    From: super_skater99@gmail.com
    Hey, I bought the premium dashboard sub yesterday (Inv #90812). It charged my visa 
    forty-nine dollars but my account still says basic!! Fix this or i want a complete 
    refund by tonight. Phone is 555-9821.
    """
    
    # File 2: A chaotic customer service phone transcript
    transcript_content = """
    TRANSCRIPT // CALL ID: 44102 // TIME: 11:04 AM
    Agent (Sarah): Thanks for calling Alpha Tech. How can I help?
    Caller (Robert Chen): Yeah hi, my company Chen Manufacturing needs a bulk quote for 
    150 units of the industrial sensors. Our maximum allocation is around $12,000. 
    Can you send an official document to r.chen@chenmills.com?
    Agent (Sarah): Absolutely, Robert. I will flag this for management.
    """

    # File 3: A generic website contact form submission
    form_content = """
    --- SITE LANDING PAGE SUBMISSION ---
    Visitor Name: Amanda Ross
    Message: Just wanted to say the new update looks great! No issues at all, 
    the software runs twice as fast on my Linux machine. Keep up the amazing work!
    Contact back: amanda@ross-design.co
    """

    files = {
        "incoming_msg_99.txt": email_content,
        "call_audio_trans_44102.log": transcript_content,
        "web_form_dump_alpha.data": form_content
    }

    for filename, content in files.items():
        with open(os.path.join(INPUT_DIR, filename), "w") as f:
            f.write(content.strip())
            
    print(f"[SUCCESS] Generated {len(files)} chaotic data files inside '{INPUT_DIR}'")

if __name__ == "__main__":
    generate_sandbox()