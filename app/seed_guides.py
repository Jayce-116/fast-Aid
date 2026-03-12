from app.database import SessionLocal, Base, engine
from app.models.guide import Guide
import json

# ---- COMPREHENSIVE FIRST AID GUIDE DATABASE ----
first_aid_data = [
    # ========== BLEEDING ==========
    {
        "title": "Severe Bleeding Control",
        "summary": "How to stop heavy external bleeding and prevent shock.",
        "category": "Bleeding",
        "urgency": "Critical",
        "estimated_time": "5–7 minutes",
        "symptoms": ["Heavy blood loss", "Pale skin", "Rapid pulse", "Dizziness"],
        "donts": ["Do not remove the cloth once applied", "Do not apply a tourniquet unless bleeding won't stop"],
        "steps": [
            "Apply firm direct pressure with a clean cloth.",
            "Do NOT remove the cloth; add more layers if soaked.",
            "Elevate the injured limb if no fracture is suspected.",
            "If bleeding continues, apply a pressure bandage.",
            "Apply a tourniquet only as a last resort.",
            "Monitor for signs of shock (pale, weak, confused).",
            "Call 911 immediately."
        ]
    },
    {
        "title": "Nosebleed (Epistaxis)",
        "summary": "Stop mild to moderate nosebleeds quickly.",
        "category": "Bleeding",
        "urgency": "Mild",
        "estimated_time": "3–5 minutes",
        "symptoms": ["Blood from nose", "Blood in throat"],
        "donts": ["Do not tilt head backward", "Do not blow nose immediately"],
        "steps": [
            "Sit upright and lean slightly forward.",
            "Pinch the soft part of the nose for 10–15 minutes.",
            "Apply a cold compress to the nose bridge.",
            "Breathe through your mouth.",
            "Do not blow nose for several hours.",
            "Seek care if bleeding persists after 20 minutes."
        ]
    },
    {
        "title": "Internal Bleeding Suspicion",
        "summary": "Recognize and respond to suspected internal bleeding.",
        "category": "Bleeding",
        "urgency": "Critical",
        "estimated_time": "Immediate – call 911",
        "symptoms": ["Abdominal pain", "Bruising", "Coughing or vomiting blood", "Pale/clammy skin"],
        "donts": ["Do not give food or water", "Do not apply pressure to the abdomen"],
        "steps": [
            "Call 911 immediately.",
            "Keep the person lying down and still.",
            "Elevate legs slightly unless head/neck/back injury suspected.",
            "Keep them warm with a blanket.",
            "Monitor breathing and pulse until help arrives."
        ]
    },
    # ========== BURNS ==========
    {
        "title": "Minor Burn (First-Degree)",
        "summary": "Cool and treat superficial burn injuries.",
        "category": "Burn",
        "urgency": "Mild",
        "estimated_time": "3–5 minutes",
        "symptoms": ["Redness", "Tenderness", "Swelling"],
        "donts": ["Do not apply ice", "Do not use butter or toothpaste", "Do not pop blisters"],
        "steps": [
            "Cool the burn with cool (not cold) running water for 10 minutes.",
            "Remove tight clothing or jewelry near the area.",
            "Do NOT apply ice, oil, or toothpaste.",
            "Cover loosely with sterile gauze or clean cloth.",
            "Take over-the-counter pain reliever if needed."
        ]
    },
    {
        "title": "Second-Degree Burn",
        "summary": "Manage blistering burn injuries safely.",
        "category": "Burn",
        "urgency": "Moderate",
        "estimated_time": "5–8 minutes",
        "symptoms": ["Blisters", "Deep redness", "Wet/shiny skin", "Severe pain"],
        "donts": ["Do not pop blisters", "Do not use ice"],
        "steps": [
            "Cool the burn under running water for 15 minutes.",
            "Do NOT pop blisters.",
            "Cover with sterile, non-stick dressing.",
            "Take pain relievers if needed.",
            "Seek medical care for large or infected burns.",
            "Do not remove clothing stuck to the burn."
        ]
    },
    {
        "title": "Third-Degree Burn",
        "summary": "Life-threatening burn requiring immediate emergency care.",
        "category": "Burn",
        "urgency": "Critical",
        "estimated_time": "Immediate – call 911",
        "symptoms": ["White or charred skin", "No pain (nerve damage)", "Leathery skin texture"],
        "donts": ["Do not apply water", "Do not remove clothing", "Do not apply any creams"],
        "steps": [
            "Call 911 immediately.",
            "Do NOT apply water, ice, or any substance.",
            "Do NOT remove burned clothing.",
            "Cover loosely with a clean non-stick dressing or foil.",
            "Monitor for shock and keep the person warm.",
            "Do not let the person drink anything."
        ]
    },
    {
        "title": "Chemical Burn",
        "summary": "Treat burns caused by acids, alkalis, or household chemicals.",
        "category": "Burn",
        "urgency": "Critical",
        "estimated_time": "10–15 minutes",
        "symptoms": ["Burning pain", "Skin discoloration", "Swelling"],
        "donts": ["Do not rub the affected area", "Do not apply neutralizing agents"],
        "steps": [
            "Remove contaminated clothing immediately, wearing gloves if available.",
            "Flush the affected area with large amounts of water for at least 20 minutes.",
            "Call 911 or Poison Control.",
            "If the chemical is in the eyes, flush continuously with water for 20 minutes.",
            "Take the chemical container to the emergency room for identification."
        ]
    },
    # ========== CARDIAC ==========
    {
        "title": "Cardiac Arrest – CPR (Adult)",
        "summary": "Perform CPR on an unresponsive adult with no pulse.",
        "category": "Cardiac",
        "urgency": "Critical",
        "estimated_time": "Until help arrives",
        "symptoms": ["Unresponsive", "No breathing", "No pulse"],
        "donts": ["Do not stop CPR until paramedics arrive", "Do not move the person unnecessarily"],
        "steps": [
            "Call 911 immediately or ask someone nearby to call.",
            "Check for responsiveness by tapping the shoulders and shouting.",
            "If no response, lay the person flat on their back on a firm surface.",
            "Tilt head back and lift chin to open airway.",
            "Check for breathing for 10 seconds.",
            "Begin chest compressions: place hands on center of chest, press down 2 inches at 100–120 compressions/min.",
            "After 30 compressions, give 2 rescue breaths.",
            "Continue until an AED arrives or paramedics take over.",
            "Use AED as soon as available – follow device voice prompts."
        ]
    },
    {
        "title": "Cardiac Arrest – CPR (Child)",
        "summary": "Perform CPR on an unresponsive child aged 1–8 years.",
        "category": "Cardiac",
        "urgency": "Critical",
        "estimated_time": "Until help arrives",
        "symptoms": ["Unresponsive", "Not breathing normally", "No pulse"],
        "donts": ["Do not use full adult force for compressions"],
        "steps": [
            "Call 911. If alone with child, give 2 minutes of CPR first then call.",
            "Lay the child on a firm flat surface.",
            "Tilt head back slightly and lift chin to open airway.",
            "Give 2 gentle rescue breaths, watching for chest rise.",
            "Do 30 chest compressions using 2 hands or 1 hand (heel) at 2 inches deep.",
            "Continue 30:2 ratio until help arrives or the child recovers."
        ]
    },
    {
        "title": "Heart Attack Recognition and Response",
        "summary": "Identify and respond to a heart attack quickly.",
        "category": "Cardiac",
        "urgency": "Critical",
        "estimated_time": "Immediate – call 911",
        "symptoms": ["Chest pain or tightness", "Pain in arm/jaw/back", "Shortness of breath", "Sweating", "Nausea"],
        "donts": ["Do not let the person drive themselves to hospital", "Do not give aspirin if allergic"],
        "steps": [
            "Call 911 immediately.",
            "Have the person sit or lie down comfortably.",
            "Loosen any tight clothing.",
            "If the person is not allergic and conscious, give a regular aspirin to chew.",
            "If they become unresponsive and aren't breathing, begin CPR.",
            "Use AED if available."
        ]
    },
    # ========== CHOKING ==========
    {
        "title": "Choking – Adult",
        "summary": "Dislodge a foreign object from an adult's airway.",
        "category": "Choking",
        "urgency": "Critical",
        "estimated_time": "1–3 minutes",
        "symptoms": ["Holding throat", "High-pitched wheezing", "Bluish lips", "Cannot speak or cough"],
        "donts": ["Do not perform blind finger sweeps", "Do not do abdominal thrusts on pregnant women"],
        "steps": [
            "Ask: 'Are you choking?' If they cannot speak, act immediately.",
            "Stand behind the person. Place one foot forward for support.",
            "Give 5 firm back blows between the shoulder blades with the heel of your hand.",
            "If unsuccessful, perform abdominal thrusts (Heimlich maneuver): wrap arms around waist, make fist above navel, thrust sharply inward and upward.",
            "Alternate 5 back blows and 5 abdominal thrusts until the object clears.",
            "If the person becomes unconscious, call 911 and begin CPR."
        ]
    },
    {
        "title": "Choking – Infant (Under 1 year)",
        "summary": "Clear airway blockage in a baby or infant.",
        "category": "Choking",
        "urgency": "Critical",
        "estimated_time": "1–2 minutes",
        "symptoms": ["Cannot cry or make sounds", "Weak cough", "Bluish skin"],
        "donts": ["Do not do abdominal thrusts on infants", "Do not do blind sweeps in infant's mouth"],
        "steps": [
            "Hold the infant face-down on your forearm supporting the head.",
            "Give 5 gentle back blows between the shoulder blades.",
            "Flip infant face-up on your forearm.",
            "Give 5 chest thrusts with 2 fingers on the center of the chest.",
            "Repeat back blows and chest thrusts until the object clears or infant becomes unconscious.",
            "If unconscious, call 911 and start infant CPR."
        ]
    },
    {
        "title": "Choking – Pregnant or Obese Person",
        "summary": "Adapt the Heimlich maneuver for pregnancy or obesity.",
        "category": "Choking",
        "urgency": "Critical",
        "estimated_time": "1–3 minutes",
        "symptoms": ["Holding throat", "Cannot speak", "Severe distress"],
        "donts": ["Do not compress the abdomen"],
        "steps": [
            "Stand behind the person and place your arms under their armpits.",
            "Position your hands on the center of the chest (breastbone).",
            "Give firm chest thrusts straight backward.",
            "Alternate with 5 back blows.",
            "If unconscious, call 911 and begin modified CPR."
        ]
    },
    # ========== FRACTURES ==========
    {
        "title": "Broken Bone (Fracture)",
        "summary": "Stabilize a suspected fracture until medical help arrives.",
        "category": "Fracture",
        "urgency": "Moderate",
        "estimated_time": "5–10 minutes",
        "symptoms": ["Visible deformity", "Intense pain", "Swelling", "Inability to move"],
        "donts": ["Do not try to realign the bone", "Do not move person unnecessarily"],
        "steps": [
            "Stop any bleeding: apply gentle pressure with a clean bandage.",
            "Immobilize the injured area using a splint (rolled magazine, sticks, or boards).",
            "Apply ice wrapped in cloth to reduce swelling.",
            "Do NOT try to straighten the bone.",
            "Elevate the injury if possible.",
            "Seek immediate medical attention."
        ]
    },
    {
        "title": "Suspected Spinal Injury",
        "summary": "Minimize movement for potential spinal cord injuries.",
        "category": "Fracture",
        "urgency": "Critical",
        "estimated_time": "Immediate – call 911",
        "symptoms": ["Neck/back pain after impact", "Numbness in limbs", "Inability to move arms or legs"],
        "donts": ["Do not move the person", "Do not remove helmet if wearing one"],
        "steps": [
            "Call 911 immediately.",
            "Tell the person to stay still.",
            "If breathing, do not move them — stabilize the head and neck in the position found.",
            "If unconscious but breathing, do not move unless immediate danger (fire/water).",
            "If CPR is needed, keep head/neck neutral while performing compressions.",
            "Wait for paramedics — do not attempt to transport."
        ]
    },
    {
        "title": "Dislocated Joint",
        "summary": "Respond to a shoulder, knee, or finger dislocation.",
        "category": "Fracture",
        "urgency": "Moderate",
        "estimated_time": "5–10 minutes",
        "symptoms": ["Visible joint deformity", "Severe pain", "Swelling", "Limited range of motion"],
        "donts": ["Do not try to put bone back in place", "Do not apply heat"],
        "steps": [
            "Immobilize the joint in the position it is found.",
            "Apply ice wrapped in cloth for 20 minutes.",
            "Elevate the limb if possible.",
            "Do NOT attempt to relocate the joint yourself.",
            "Seek emergency medical care immediately."
        ]
    },
    # ========== POISONING ==========
    {
        "title": "Suspected Poisoning",
        "summary": "Respond to accidental ingestion of a toxic substance.",
        "category": "Poisoning",
        "urgency": "Critical",
        "estimated_time": "Immediate",
        "symptoms": ["Nausea/vomiting", "Seizures", "Confusion", "Burns around mouth"],
        "donts": ["Do not induce vomiting unless directed by Poison Control", "Do not give food or water"],
        "steps": [
            "Call 911 or Poison Control (1-800-222-1222) immediately.",
            "Stay calm and provide the substance name if known.",
            "Do NOT induce vomiting unless specifically instructed by Poison Control.",
            "If conscious, keep the person upright.",
            "If unconscious, place in recovery position.",
            "Bring the container/label to the hospital."
        ]
    },
    {
        "title": "Alcohol Poisoning",
        "summary": "Respond to severe alcohol intoxication.",
        "category": "Poisoning",
        "urgency": "Critical",
        "estimated_time": "Immediate – call 911",
        "symptoms": ["Confusion", "Vomiting", "Seizures", "Slow breathing", "Blue-tinged lips"],
        "donts": ["Do not leave the person alone", "Do not give coffee or food"],
        "steps": [
            "Call 911 immediately for severe symptoms.",
            "Keep the person sitting upright or in the recovery position.",
            "If unconscious and breathing, place on their side to prevent choking.",
            "Do NOT give coffee or water — it won't sober them up faster.",
            "Monitor breathing and pulse.",
            "Stay with them until help arrives."
        ]
    },
    {
        "title": "Drug Overdose",
        "summary": "Recognize and respond to an opioid or medication overdose.",
        "category": "Poisoning",
        "urgency": "Critical",
        "estimated_time": "Immediate – call 911",
        "symptoms": ["Unresponsive", "Slow or stopped breathing", "Pinpoint pupils", "Blue lips/nails"],
        "donts": ["Do not leave the person alone", "Do not try to make them vomit"],
        "steps": [
            "Call 911 immediately.",
            "If naloxone (Narcan) is available, administer it.",
            "If not breathing, begin rescue breathing or CPR.",
            "Place in recovery position if breathing.",
            "Stay with the person until help arrives.",
            "Do not leave them alone even if they appear to improve."
        ]
    },
    # ========== ANAPHYLAXIS ==========
    {
        "title": "Anaphylaxis (Severe Allergic Reaction)",
        "summary": "Emergency response to life-threatening allergy.",
        "category": "Anaphylaxis",
        "urgency": "Critical",
        "estimated_time": "Immediate",
        "symptoms": ["Swollen throat/tongue", "Difficulty breathing", "Hives/itching", "Rapid pulse", "Dizziness"],
        "donts": ["Do not delay epinephrine", "Do not have the person stand up"],
        "steps": [
            "Call 911 immediately.",
            "Use an epinephrine auto-injector (EpiPen) — inject into outer thigh.",
            "Have the person lie down with legs elevated (unless breathing is difficult).",
            "If breathing is difficult, allow them to sit upright.",
            "A second epinephrine dose may be given after 5–15 minutes if needed.",
            "Even after improvement, they must go to the hospital immediately."
        ]
    },
    # ========== DROWNING ==========
    {
        "title": "Near-Drowning / Water Rescue",
        "summary": "Respond to someone pulled from water.",
        "category": "Drowning",
        "urgency": "Critical",
        "estimated_time": "Immediate",
        "symptoms": ["Unresponsive", "Not breathing", "Blue lips", "Coughing up water"],
        "donts": ["Do not enter deep water without training", "Do not shake the victim"],
        "steps": [
            "Ensure your own safety — don't jump in unless trained.",
            "Extend a rope, towel, or object for the victim to grab, or throw a floatation device.",
            "Once on dry land, call 911 immediately.",
            "Check for breathing and pulse.",
            "Begin CPR if not breathing — do NOT skip rescue breaths for drowning victims.",
            "Keep the person warm to prevent hypothermia.",
            "Even if they appear recovered, take them to hospital."
        ]
    },
    # ========== SEIZURES ==========
    {
        "title": "Seizure (Epileptic Fit)",
        "summary": "Protect a seizure victim from injury.",
        "category": "Seizure",
        "urgency": "Moderate",
        "estimated_time": "Duration of seizure",
        "symptoms": ["Convulsions", "Loss of consciousness", "Jerking movements", "Confusion after"],
        "donts": ["Do not hold person down", "Do not put anything in their mouth", "Do not give water during seizure"],
        "steps": [
            "Stay calm and time the seizure.",
            "Clear the area of hard or sharp objects.",
            "Place something soft under their head.",
            "Turn them on their side after convulsions stop to prevent choking.",
            "Do NOT restrain the person or put anything in their mouth.",
            "Call 911 if: seizure lasts over 5 minutes, person doesn't regain consciousness, or it's their first seizure.",
            "Stay with them until fully awake and oriented."
        ]
    },
    # ========== STROKE ==========
    {
        "title": "Stroke – FAST Recognition",
        "summary": "Identify and respond to a stroke using FAST method.",
        "category": "Stroke",
        "urgency": "Critical",
        "estimated_time": "Immediate – call 911",
        "symptoms": ["Facial drooping", "Arm weakness", "Speech difficulty", "Sudden severe headache"],
        "donts": ["Do not give food or water", "Do not let the person sleep it off"],
        "steps": [
            "Use FAST: Face (drooping?), Arms (one weak?), Speech (slurred?), Time (call 911).",
            "Call 911 immediately — time is critical.",
            "Note the time symptoms started.",
            "Keep the person calm and lying down.",
            "Do not give food, water, or any medication.",
            "Loosen tight clothing.",
            "If unconscious and not breathing, begin CPR."
        ]
    },
    # ========== HYPOTHERMIA / HEAT ==========
    {
        "title": "Hypothermia",
        "summary": "Treat dangerously low body temperature.",
        "category": "Environmental",
        "urgency": "Critical",
        "estimated_time": "10–20 minutes",
        "symptoms": ["Shivering", "Confusion", "Slurred speech", "Drowsiness", "Weak pulse"],
        "donts": ["Do not rub limbs vigorously", "Do not give alcohol"],
        "steps": [
            "Move the person out of the cold immediately.",
            "Remove wet clothing gently.",
            "Cover with blankets, especially head and neck.",
            "Place warm (not hot) water bottles wrapped in cloth near the groin, armpits, and neck.",
            "Give warm, non-alcoholic beverages if alert.",
            "Call 911 for severe hypothermia.",
            "If unconscious, begin CPR if needed."
        ]
    },
    {
        "title": "Heat Stroke",
        "summary": "Treat life-threatening overheating of the body.",
        "category": "Environmental",
        "urgency": "Critical",
        "estimated_time": "Immediate",
        "symptoms": ["Body temp above 104°F (40°C)", "No sweating", "Confusion", "Rapid heart rate"],
        "donts": ["Do not give medication", "Do not leave alone"],
        "steps": [
            "Call 911 immediately.",
            "Move the person to a cool, shaded area.",
            "Remove excess clothing.",
            "Cool them rapidly: apply ice packs to neck, armpits, groin; fan them; spray cool water.",
            "Do NOT give fluids if they are confused or unconscious.",
            "If conscious and able to swallow, give cool water to drink.",
            "Monitor until help arrives."
        ]
    },
    {
        "title": "Heat Exhaustion",
        "summary": "Respond to overheating with heavy sweating and weakness.",
        "category": "Environmental",
        "urgency": "Moderate",
        "estimated_time": "10–15 minutes",
        "symptoms": ["Heavy sweating", "Weakness", "Cool/pale skin", "Fast/weak pulse", "Nausea"],
        "donts": ["Do not give sugary or caffeinated drinks", "Do not ignore symptoms"],
        "steps": [
            "Move the person to a cool, shaded, or air-conditioned environment.",
            "Have them lie down and elevate their legs.",
            "Remove tight or excess clothing.",
            "Apply cool, wet cloths to skin.",
            "Give sips of cool water if alert and not nauseous.",
            "Seek medical help if symptoms worsen or last more than 1 hour."
        ]
    },
    # ========== EYE ==========
    {
        "title": "Foreign Object in Eye",
        "summary": "Safely remove a particle or debris from the eye.",
        "category": "Eye",
        "urgency": "Moderate",
        "estimated_time": "3–5 minutes",
        "symptoms": ["Eye irritation", "Tearing", "Redness", "Visible particle"],
        "donts": ["Do not rub the eye", "Do not try to remove embedded objects"],
        "steps": [
            "Do NOT rub the eye.",
            "Wash your hands before touching the eye.",
            "Blink several times to try to wash out the object naturally.",
            "Gently flush the eye with clean water for 15 minutes using an eye wash or cup.",
            "If the object is under the eyelid, lift the lid gently and use a damp cotton swab.",
            "If the object is embedded or vision is affected, cover the eye and go to hospital."
        ]
    },
    {
        "title": "Chemical Splash in Eye",
        "summary": "Emergency flushing for chemical eye exposure.",
        "category": "Eye",
        "urgency": "Critical",
        "estimated_time": "Immediate",
        "symptoms": ["Burning pain", "Redness", "Vision changes"],
        "donts": ["Do not rub the eye", "Do not delay flushing"],
        "steps": [
            "Immediately flush the eye with clean water for at least 20 minutes continuously.",
            "Hold eyelid open to ensure eye is fully rinsed.",
            "If wearing contact lenses, remove them if possible without interrupting flushing.",
            "Call 911 or Poison Control.",
            "Go to the emergency room after flushing."
        ]
    },
    # ========== BITES & STINGS ==========
    {
        "title": "Snake Bite",
        "summary": "Respond to a snake bite to minimize venom spread.",
        "category": "Bites",
        "urgency": "Critical",
        "estimated_time": "Immediate – call 911",
        "symptoms": ["Pain at bite site", "Swelling", "Nausea", "Dizziness", "Fang marks"],
        "donts": ["Do not suck out venom", "Do not apply tourniquet", "Do not cut the bite"],
        "steps": [
            "Call 911 or get to the nearest hospital immediately.",
            "Keep the person calm and still — movement spreads venom.",
            "Remove watches, rings, or tight clothing near the bite.",
            "Keep the bitten limb below heart level.",
            "Note the snake's appearance if safe to do so.",
            "Do NOT suck out venom, cut the bite, or apply ice or tourniquet."
        ]
    },
    {
        "title": "Dog Bite",
        "summary": "Clean and treat a dog bite wound.",
        "category": "Bites",
        "urgency": "Moderate",
        "estimated_time": "5–10 minutes",
        "symptoms": ["Puncture wounds", "Laceration", "Bleeding", "Swelling"],
        "donts": ["Do not ignore the wound even if small"],
        "steps": [
            "If bleeding, apply pressure with a clean cloth.",
            "Wash the wound thoroughly with soap and water for at least 5 minutes.",
            "Apply antibiotic ointment.",
            "Cover with a sterile bandage.",
            "Seek medical attention for deep bites, bites to face/hands, or unknown rabies status.",
            "Report the bite to local animal control."
        ]
    },
    {
        "title": "Bee or Wasp Sting",
        "summary": "Treat a bee or wasp sting and watch for allergic reaction.",
        "category": "Bites",
        "urgency": "Mild",
        "estimated_time": "3–5 minutes",
        "symptoms": ["Sharp pain", "Swelling", "Redness", "Itching"],
        "donts": ["Do not squeeze the venom sac", "Do not scratch the area"],
        "steps": [
            "Remove the stinger by scraping with a flat edge (credit card) — don't squeeze it.",
            "Wash the area with soap and water.",
            "Apply a cold pack wrapped in cloth for 20 minutes.",
            "Take antihistamine for itching.",
            "Watch for signs of allergic reaction: hives, swelling of throat, difficulty breathing.",
            "If allergic reaction occurs, use EpiPen and call 911 immediately."
        ]
    },
    {
        "title": "Spider Bite",
        "summary": "Handle a spider bite safely, especially black widow or brown recluse.",
        "category": "Bites",
        "urgency": "Moderate",
        "estimated_time": "5–10 minutes",
        "symptoms": ["Pain at site", "Redness", "Swelling", "Muscle cramps", "Nausea"],
        "donts": ["Do not apply a tourniquet", "Do not suck out venom"],
        "steps": [
            "Wash the bite area with soap and water.",
            "Apply ice pack wrapped in cloth for 10 minutes.",
            "Keep the affected limb elevated.",
            "Take a pain reliever if needed.",
            "Seek medical help promptly for suspected black widow or brown recluse bites.",
            "Bring the spider to hospital if captured safely."
        ]
    },
    # ========== HEAD / CONCUSSION ==========
    {
        "title": "Head Injury and Concussion",
        "summary": "Assess and respond to a blow to the head.",
        "category": "Head Injury",
        "urgency": "Moderate",
        "estimated_time": "10–15 minutes",
        "symptoms": ["Headache", "Confusion", "Dizziness", "Nausea", "Memory loss", "Unequal pupils"],
        "donts": ["Do not leave alone", "Do not let them sleep without checking every 2 hours"],
        "steps": [
            "Call 911 if: loss of consciousness, seizure, repeated vomiting, severe headache.",
            "Have the person sit or lie quietly in a well-lit area.",
            "Apply ice wrapped in cloth to any swelling — 20 min on, 20 min off.",
            "Do NOT give pain medications that thin the blood (aspirin, ibuprofen).",
            "Monitor for worsening symptoms over the next 24–48 hours.",
            "Avoid physical or mental activity until cleared by a doctor."
        ]
    },
    # ========== DIABETIC ==========
    {
        "title": "Low Blood Sugar (Hypoglycemia)",
        "summary": "Respond to dangerously low blood glucose levels.",
        "category": "Diabetic",
        "urgency": "Moderate",
        "estimated_time": "5–10 minutes",
        "symptoms": ["Shakiness", "Sweating", "Confusion", "Pale skin", "Rapid heartbeat", "Fainting"],
        "donts": ["Do not give food or drink if unconscious"],
        "steps": [
            "If conscious and able to swallow, give 15–20g of fast-acting sugar: glucose tablets, juice, or regular soda.",
            "Wait 15 minutes and recheck blood sugar.",
            "If improved, give a snack or meal.",
            "If unconscious or unable to swallow, call 911 — do NOT give anything by mouth.",
            "If glucagon kit available, administer per instructions."
        ]
    },
    {
        "title": "High Blood Sugar (Hyperglycemia)",
        "summary": "Recognize and respond to elevated blood glucose levels.",
        "category": "Diabetic",
        "urgency": "Moderate",
        "estimated_time": "Varies",
        "symptoms": ["Increased thirst", "Frequent urination", "Fatigue", "Blurred vision", "Fruity breath"],
        "donts": ["Do not delay medical care if DKA is suspected"],
        "steps": [
            "Encourage the person to drink water to prevent dehydration.",
            "If they take insulin, they should follow their prescribed correction plan.",
            "Monitor blood sugar every 1–2 hours.",
            "If blood sugar is above 300 mg/dL or symptoms worsen, seek emergency care.",
            "Call 911 if: vomiting, severe abdominal pain, fruity breath (signs of diabetic ketoacidosis – DKA)."
        ]
    },
    # ========== ASTHMA ==========
    {
        "title": "Asthma Attack",
        "summary": "Help someone through a sudden asthma attack.",
        "category": "Breathing",
        "urgency": "Moderate",
        "estimated_time": "3–10 minutes",
        "symptoms": ["Wheezing", "Shortness of breath", "Coughing", "Chest tightness"],
        "donts": ["Do not leave them alone", "Do not lay them down flat"],
        "steps": [
            "Help the person sit upright and lean slightly forward.",
            "Help them use their prescribed rescue inhaler (usually blue, e.g., Albuterol).",
            "Shake inhaler well, have them breathe in slowly while pressing down.",
            "If no improvement after 4 puffs, call 911.",
            "Keep them calm and remove any triggers (smoke, dust).",
            "Monitor breathing rate and call 911 if they cannot speak or are turning blue."
        ]
    },
    # ========== FAINTING ==========
    {
        "title": "Fainting (Syncope)",
        "summary": "Respond to someone who has fainted or is about to faint.",
        "category": "Fainting",
        "urgency": "Mild",
        "estimated_time": "3–5 minutes",
        "symptoms": ["Sudden loss of consciousness", "Pale/sweaty skin", "Weak pulse"],
        "donts": ["Do not prop in sitting position if unconscious", "Do not splash water on face"],
        "steps": [
            "If about to faint: have them lie down and elevate legs 12 inches.",
            "Loosen any tight clothing (belt, tie, collar).",
            "Ensure good airflow — open windows or use a fan.",
            "If already fainted, check for responsiveness and breathing.",
            "If breathing, place in recovery position.",
            "Call 911 if they don't regain consciousness within 1 minute or have a history of heart problems."
        ]
    },
    # ========== MENTAL ==========
    {
        "title": "Panic Attack",
        "summary": "Support someone experiencing a panic attack.",
        "category": "Mental Health",
        "urgency": "Mild",
        "estimated_time": "5–20 minutes",
        "symptoms": ["Racing heart", "Shortness of breath", "Trembling", "Feeling of doom", "Chest pain"],
        "donts": ["Do not dismiss their feelings", "Do not leave them alone"],
        "steps": [
            "Stay calm and speak in a slow, reassuring tone.",
            "Guide them to a quiet area if possible.",
            "Encourage slow, controlled breathing: breathe in for 4 counts, hold 4, out for 6.",
            "Help them focus on physical sensations (feel feet on floor, describe 5 things they see).",
            "Do NOT say 'calm down' — instead try: 'You're safe, I'm here with you.'",
            "If symptoms don't improve or chest pain is severe, call 911 to rule out cardiac event."
        ]
    },
    # ========== VEHICLE ACCIDENT ==========
    {
        "title": "Car/Vehicle Accident First Response",
        "summary": "Initial response to a road traffic accident.",
        "category": "Trauma",
        "urgency": "Critical",
        "estimated_time": "Immediate – call 911",
        "symptoms": ["Bleeding", "Unconsciousness", "Trapped victims", "Crash damage"],
        "donts": ["Do not move injured persons unless in immediate danger of fire/explosion", "Do not remove helmets"],
        "steps": [
            "Ensure scene safety — turn on hazard lights and keep a safe distance.",
            "Call 911 immediately.",
            "Check each person: are they conscious? Breathing?",
            "Control severe bleeding with direct pressure.",
            "Do NOT move anyone with a potential spinal injury.",
            "Turn off engines to reduce fire risk if you can do so safely.",
            "Use warning triangles to alert oncoming traffic.",
            "Stay with victims and provide reassurance until help arrives."
        ]
    },
    # ========== PREGNANCY ==========
    {
        "title": "Emergency Childbirth",
        "summary": "Assist with an unexpected delivery when medical help isn't available.",
        "category": "Pregnancy",
        "urgency": "Critical",
        "estimated_time": "Varies",
        "symptoms": ["Active labor contractions", "Water has broken", "Baby crowning"],
        "donts": ["Do not pull on the baby", "Do not cut the umbilical cord unless instructed"],
        "steps": [
            "Call 911 immediately — tell them a baby is coming.",
            "Help the mother lie on her back with knees bent.",
            "Support the baby's head as it emerges — do not pull.",
            "Gently clean the baby's mouth and nose with a clean cloth.",
            "Keep the baby warm by wrapping in clean blankets or clothes.",
            "Do not cut the umbilical cord unless professionally instructed.",
            "Keep both mother and baby warm until paramedics arrive."
        ]
    },
    # ========== MENTAL HEALTH ==========
    {
        "title": "Suicidal Crisis Response",
        "summary": "Support someone in a suicidal crisis safely and compassionately.",
        "category": "Mental Health",
        "urgency": "Critical",
        "estimated_time": "Ongoing",
        "symptoms": ["Talking about suicide", "Giving away possessions", "Extreme hopelessness"],
        "donts": ["Do not leave them alone", "Do not dismiss their feelings", "Do not be judgmental"],
        "steps": [
            "Stay calm and listen without judgment.",
            "Ask directly: 'Are you thinking about suicide?' — this does NOT increase risk.",
            "Do not leave them alone if immediate risk.",
            "Remove access to potential means (medications, weapons) if safe to do so.",
            "Call a crisis line: 988 Suicide & Crisis Lifeline.",
            "Call 911 if there is immediate danger.",
            "Stay with them and reassure them that help is available."
        ]
    },
]

# ---------------- INSERT DATA -----------------

def seed_database():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    # clear old data
    db.query(Guide).delete()
    db.commit()

    # insert new data
    for guide in first_aid_data:
        db.add(
            Guide(
                title=guide["title"],
                summary=guide["summary"],
                category=guide["category"],
                urgency=guide.get("urgency", "Moderate"),
                estimated_time=guide["estimated_time"],
                steps=json.dumps(guide["steps"]),
                symptoms=json.dumps(guide.get("symptoms", [])),
                donts=json.dumps(guide.get("donts", []))
            )
        )

    db.commit()
    db.close()
    print(f"Inserted {len(first_aid_data)} guides successfully!")

if __name__ == "__main__":
    seed_database()