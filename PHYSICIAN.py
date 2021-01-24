#PHYSICIAN
import time

#MEETING
print("Hi, I'm Physician")
print("I was built by Jessé Alves Leite, born in Sao Paulo, Brazil, 1998 and I can do all what a physician does, except for surgeries.\nPlease, type 'medical advice', keep rewriting,then hit enter")
print("Check out: 'https://jessealvesleitesoftwares.company.site'")

#ALGORITHMS
y = 0
while y < 100:
    i = input()
    if i == 'medical advice':
        print("write/say basic symptoms, emergence, first aid, poisons, diagnosis(symptoms in alphabetical order), tests(disease) treatment(disease), laboratory tests, advanced symptoms, derived diseases,  immortal")
    elif i == "basic symptoms":
        myLabel = Label(root, text="write diagnosis abdominal pain, diagnosis chest pain, diagnosis cough, diagnosis diarrhea, diagnosis dizziness, diagnosis headache, diagnosis joint pain, diagnosis low back pain,\ndiagnosis painful shoulder, diagnosis rectal bleeding, diagnosis sore throat, diagnosis urinary frequency and burning, diagnosis vaginal discharge")
    elif i == "advanced symptoms":
        print("say abdominal acute pain, abdominal pain chronic recurrent, abdominal rigidity, abdominal swelling focal, abdominal swelling generalized, absent or diminished pulse, acid phosphatase elevation, acidosis, alkaline phosphatase elevation, alkalosis, alopecia, iron serum, serum uric acid, amenorrhea, amnesia, anemia, ankle clonus, anorexia, anosmia or unusual odors, anuria or oliguria, anxiety, aphasia apraxia and agnosia, ascites, aspartate aminotransferase elevation, ataxia, axillary mass, Babinski's sign, back pain, bleeding gums, blindness, blurred vision, bone mass or swelling, borborygmi, bradycardia, breast discharge, breast mass, breast pain, cardiac arrhythmia, cardiac murmurs, cardiomegaly, chest pain, chest tenderness, chills, choreiform movements, clubbing of the fingers, coma, constipation, convulsions or syncope, cough, cramps muscular, c-reactive protein, cyanosis, deafness, delayed puberty, delirium, delusions, dementia, depression, diaphoresis, diarrhea acute, diarrhea chronic, difficulty urinating, diplopia, dizziness, drop attacks, dwarfism, dysarthria, dysmenorrhea, dyspareunia, dysphagia, dyspnea, dysuria, ear discharge, earache, edema generalized, edema localized, enuresis, epiphora, epistaxis, euphoria, exophthalmos, extremity pain lower extremity, extremity pain upper extremity, eye pain, face pain, facial flushing, facial paralysis, facial swelling, failure to thrive, fatigue, femoral mass or swelling, fever acute, fever chronic, flank mass, flank pain, flatulence, foot and toe pain, foot deformities, foot ulceration, free thyroxine, frequency of urination, frigidity, gait disturbances, gangrene, gigantism, girdle pain, glycosuria, gynecomastia, halitosis, halucinations, headache, heartburn, heel pain, hematemesis, hematuria, hemianopsia, hemiparesis or hemiplegia, hemoptysis, hepatomegaly, hiccups, hip pain, hirsutism, hoarseness, Horner's syndrome, 25-hydroxyvitamin d2 and d3, hyperactive reflexes, hypercalcemia, hypercholesterolemia, hyperglycemia, hyperkalemia, hyperkinesis, hypernatremia, hyperpigmentation, hypersomnia, hypertension, hypertriglyceridemia a, hypertriglyceridemia b, hypoactive reflexes, hypoalbuminemia, hypocalcemia, hypochondriasis, hypoglycemia, hypokalemia, hyponatremia, hypotension chronic, hypothermia, hypoxemia, impotence, incontinence of feces, incontinence of urine, increased serum bilirubin, indigestion, infertility female, infertility male, inguinal swelling, insomnia, intermittent claudication, jaundice, jaw pain, jaw swelling, joint pain, joint swelling, knee pain, knee swelling, kyphosis, lactic dehydrogenase elevation, leg ulceration, leucocytosis, leucopenia, lip pain, lip swelling, lymphadenopathy, melena, memory loss, menorrhagia, mental retardation, meteorism, metrorrhagia, monoplegia, mouth pigmentation, muscular atrophy, musculoskeletal pain generalized, nail abnormalities, nasal discharge, nasal obstruction, nausea and vomiting, neck pain, neck stiffness, neck swelling, nightmares, nocturia, nose regurgitation of food through, nystagmus, obesity pathologic, odor, opisthotonus, pain in the penis, pallor, palpitations, papilledema, paresthesias of the lower extremity, paresthesias of the upper extremity, pathologic reflexes, pelvic mass, pelvic pain, penile sores, perineum pain, periorbital edema, photophobia, plasma cortisol, polycythemia, polydipsia, polyuria, popliteal swelling, precocious puberty, priapism, prolonged prothrombin time, proteinuria, pruritus generalized, pruritus vulvae, ptosis, ptyalism, pulse irregularity, pulses unequal, pupil abnormalities, purpura and abnormal bleeding, pyuria, rales, rash distribution, rash morphology, Raynaud's phenomena, rectal bleeding, rectal discharge, rectal mass, rectal pain, red eye, regurgitation esophageal, respiration abnormalities, restless leg syndrome, risus sardonicus, scoliosis, scotoma, scrotal swelling, sedimentation rate, sensory loss, serum albumin, shoulder pain, sleep apnea, snoring, sore throat, splenomegaly acute or subacute, splenomegaly chronic, steatorrhea, strangury, stridor, stupor, syncope, tachycardia, taste abnormalities, testicular atrophy, testicular swelling, thirst or polydipsia, thrombocytopenia, thyroid enlargement, tinnitus, tongue mass or swelling, tremor, transient ischemic attacks, uremia, vaginal bleeding, vaginal discharge, vitamin b12, vulval or vaginal mass, vulval or vaginal ulcerations, weight loss")
    elif i == "derived diseases":
        print("acne vulgaris, asthma, atrial fibrillation, carpal tunnel syndrome, cataracts, cirrhosis, congestive heart failure, neuropathy, peptic ulcer, pharyngitis, pleural effusion, recurrent renal calculi, recurrent uti, stroke, uri")
# FIRST AID
    elif i == "first aid":
        print("Call the emergence service and say: mouth to mouth resuscitaion, first aid kit, accidents prevention, drowning, stroke, cramp, electric shock, kidney stone, foreign body, cut, fainting, chocking, fractures,\ninfarction, heat stroke, intoxication and allergies, nausea and vomiting, sting, low pressure, burn, bleeding, sprain, transport wounded, asphyxiation, amputation, seizure, chest pain, alcoholic coma, bruise, dislocation or head trauma")
    elif i == "first aid kit":
        print("if you want to do a first aid kit, you must put in some bag: cotton, bandages, thermal pouch, sterile gauze compresses, adhesive dresings of various sizes/band-aid, adhesive tape, latex gloves, clean cloth, clamp, ointment dor sprains or bumps, saline 0.9%, thermometer, scissors and say necessary medicines")
    elif i == "emergence":
        print("Do the primary evaluation, I mean, check if the airways are open, if the neck is stable, if there are more than 10 breathings per minute and if there's pulse, then say emergence 2")
    elif i == "emergence 2":
        print("do the secondary evaluation, seek for abnormalities in the members, vertebral column, skin color, head, mouth bleeding, chest, chest pain, meanly if going to the mandibule or towards left arm, mental confusion, hard speech, diziness, bad breathing, bad blood circulation and fever higher than 39 Celsius degrees")
    elif i == "accidents prevention":
        print("Avoid; slippery floor, accessible cleanning products, accessible cosmetics, pans wiithout cable towards stove center, watch out children and the elderly, avoid drinking alcohol and driving (or better, drink 1 liter of alcohol per year and don't smoke); if some accident happens, be sure that you and the victim stay safe (if in the street, remember the triangle reflector and put it far behind the vehicle, don't create a traffic, for that the ambulance may arrive), keep the curious ones away, call the emergence service and say emergence or first aid in the case it happens")
    elif i == "alcoholic coma":
        print("put the sick one somewhere safe, if vomits happen, leave him sitted, if unconcious, seek help (in this case, don't give him any food nor liquid)")
    elif i == "amputation":
        print("call emergence service immediatly, try to stop the bleeding by compressing around the injury, if partial amputation, don't finish it, if total amputation, put the member in a bag and this bag inside another one with ice and leave it to the hospital")
    elif i == "asphyxiations":
        print("say Heimlich's maneuver, if it doesn't work, make a tiny hole in the victim's throat, right above the first hard part (down to up direction), in the horizontal middle and put some clean object to keep it open, like pen tube, if a BABY, put him above your arm, which must be above your legs, with his belly towards the same arm and use your other arm to push his back with steady different movements, looking to expel what's in his arm")
    elif i == "bleeding":
        print("compress the region with a gauze or clean cloth, drive the vehicle carefully; if in the nose, sit down, don't incline your head and compress your nose during 10 minutes, if it doesn't solve it, seek help; if in the eye, apply cold water and go to a hospital; if inner organ is bleeding, so lye down the victim, seek help and describe carefully all the symptoms; if there's bruise, apply cold water and take paracetamol or dipyrone, the bruise will disappear in a few days")
    elif i == "bleeding time":
        print("2 to 7 minutes")
    elif e.get() == "bruise":
        myLabel = Label(root, text="apply ice several times, if any symptom instead of bruise, seek help")
    elif e.get() == "burn":
        myLabel = Label(root, text="If first degree, put the burnt region in water during 5 minutes, a shower might be used, dry crefully the region, take paracetamol and dipyrone, you can take anti-inflammatories, but don't apply ointments or anything, if second degree out it under water by 5 minutes, cover it with gauze, apply petroleum jelly, switch the gauzes daily, put nothing elese in your skin and don't burst the bubbles, if third degree, put it under water, use gauze and seek help, if fire, keep calm and get out of where you're now, stay close to the floor (smoke goes up), don't use elevators, open windows and make noise, if any chemical product touched to your eyes, wash them with water during 5 minutes, if in skin and cloth, take off your cloth and try to not touch the substance and seek help; if your clothes are on fire, calm down, try to avoid that any fuel touches your cloth, use tissued, a blanket, water, carbonic gas if available and roll my friend, roll in the ground (not too fast), take off your cloths, carefully apply cold water in your burst skin, seek medical help and take paracetamol, dipyrone and anti-inflammatories")
    elif e.get() == "cardiac arrest":
        myLabel = Label(root, text="if the heart seems to be stopped or pumping really fast, then it's cardiac arrest or, maybe, cardiorespiratory arrest")
    elif e.get() == "cardiac massage":
        myLabel = Label(root, text="Lye down the victim, come closer to his chest's side, interlance your fingers, put your hands right above the middle of his nipples, use your weight to do 30 strong compressions, do |mouth to mouth resuscitation| and repeat this sequence until rescue arrives")
    elif e.get() == "chest pain":
        myLabel = Label(root, text="also known as angina, the victim must rest and seek help, it might be beginning of an infarction, if it happened during physical activity, take it easier")
    elif e.get() == "chocking":
        myLabel = Label(root, text="if a BABY, put him above your sitted legs, with his head towards down, secure him with one am and compress his back's middle by 25 to 50 times, if it doesn't work direct his face towards up and do the same on his belly, if it doesn't work, call emergence service and do mouth to mouth resuscitation, if light ADULT, put his belly above and towards your sitted legs and compress strongly his back's middle, if WEIGHT ADULT, position him lyed down, go up to him and compress his torax using part of your mass, if CONCIOUS ADULT, then say Heimlich's maneuver")
    elif e.get() == "cosmetics":
        myLabel = Label(root, text="go to a hospital, meanwhile, take water and common pain killers as paracetamol or dipyrone, if eye affected wash it for 5 minutes with only water")
    elif e.get() == "cramp":
        myLabel = Label(root, text="cramp is due to bad blood circulation, so stand up or change your position and slowly move your legs")
    elif e.get() == "cut":
        myLabel = Label(root, text="if the cut was made with an WEAPON, thus seek medical help, if it's a SUPERFICIAL CUT, wash your hands with soap and water, leave the victim lyed down and raise the damged member, compress the injured region with some gauze or clean cloth, until it stanches the blood, what will take less than 10 minutes and seek medical help; if KNIFE STUCK, don't pull it, tell the person to move the lest possible and seek medical service; if DEEP CUT BLEEDING, seek medical help immediatly, compress the injured region and raise the damaged member, if DEEP CUT, wash your hands with soap and water, lye down the victim, raise the injured member and compress until stanch blood, one injured person must avoid touching another person to avoid contamination and seek medical care; if SCRUB, wash your hands the best way possible, if bleeding, compress with very clean cloth or gauze, wash carefully the injury, don't apply ointment, antiseptic nor cotton, if there was contact with any rusty object or soil, if  redness, pain or swelling arieses thus seek medical service")
    elif e.get() == "drowning":
        myLabel = Label(root, text="say land care or rescue of the victim")
    elif e.get() == "electric shock":
        myLabel = Label(root, text="away the victim from the font of electricity using plastic, rubber, dry wood or a dry cloth and do the same preocedures of crowning")
    elif e.get() == "fainting":
        myLabel = Label(root, text="don't let the person fall, put him on a bed or a chair with his breast above his legs, tell him to breath; if he had already fainted, thus lye him down, assuring that his head remains steady, make sure that he cans breath and give him water with sugar or juice, except if he's diabetic")
    elif e.get() == "food intoxication":
        myLabel = Label(root, text="Take one antiallergic pill and seek help")
    elif e.get() == "foreign body":
        myLabel = Label(root, text="if you have something in your NOSE, then compress your unobstructed nostril and blow strongly through your obstructed nostril, do this until the object is expelled; if unsuccessful, seek medical help; if something in your EYE, thus wash it with plenty of water and avoid scratching them; if needed seek medical help; if in your HEARD, don't try to remove it with any pointed object to avoid tympanum drilling, seek medical help")
    elif e.get() == "fractures":
        myLabel = Label(root, text="if the fracture involves the vertebral COLUMN, call emergence service right away, only move the victim if it's really necessary, don't touch his back, neither his torax, 3 or more people will be needed to transport him very carefully, aligned and steady, the lifeguard must hold his knees and feet; do this part slowly and make sure that the vehicle doesn't shake; if in the UPPER MEMBERS, don't try to move the bones, leave the broken region immobile and ice can be used; if in the FOOT, don't move it, don't take off the shoes, some clean cloth may enroll his leg and, in any case, seel medical professionals")
    elif e.get() == "gas":
        myLabel = Label(root, text="Don't try to vomit, it'll worse the situation, seek medical help")
    elif e.get() == "head trauma":
        myLabel = Label(root, text="if the head was deformed, don't try to fix its shape and seek medical help; if there's swelling, apply ice intermittently for 5 minutes; if there's bleeding and sonolence, mental confusion, fainting, difficult to walk, vomiting, double vison, different pupils sizes, noise bleeding or ear bleeding, so seek help; if the victim is a CHILD, thus go to a hospital anyway, except if it's just a very little cut and there was none impact on the head, so wash your hands, compress softly with a gauze or clean cloth, pass none ointment or anything on the injury and if the child shows none symptom, so he's fine")
    elif e.get() == "heat stroke":
        myLabel = Label(root, text="Take off the victim's cloths or put a thin one, go to a hospital; in the meanwhile, aplly him cold water, not icy and he must not drink a lot of water")
    elif e.get() == "Heimlichs maneuver":
        myLabel = Label(root, text="Hold the person by behind, with your hands on his belly button, press your fists towardsup and inside the person, compress quickly and a bit strongly by 25 times, pause for 5 seconds and do it again, this is the Heimlichs maneuver")
    elif e.get() == "heimlichs maneuver":
        myLabel = Label(root, text="Hold the person by behind, with your hands on his belly button, press your fists towardsup and inside the person, compress quickly and a bit strongly by 25 times, pause for 5 seconds and do it again, this is the Heimlichs maneuver")
    elif e.get() == "infarction":
        myLabel = Label(root, text="First of all, give ACETILSALICILIC ACID to the victim, if he's alergic, so drive him (or take a ride/taxi etc) to the nearest hospital; while waiting, loosen his cloths, try to keep him calm, he must not make any effort, say cardiac arrest to know if that's also the situation; if it is, then start cardiac massage, just say cardiac massage")
    elif e.get() == "land care":
        myLabel = Label(root, text="Do mouth breathing, 2 blows and 1 little interval; if the person has a cardiac arrest (say cardiac arrest to know how to identify it), then do the resuscitation, by pressing the chest intermittently")
    elif e.get() == "low blood pressure":
        myLabel = Label(root, text="Lye down, take little amounts os liquids, be sure if you didn't forget to take any medicine, if you haven't eaten for a while, so take a fruits juice, if weakness and fainting feelings appears for more than 15 minutes, thus seek help")
    elif e.get() == "mouth to mouth resuscitation":
        myLabel = Label(root, text="You don't have to do his maneuver, due to the risk of infection; if you wanna do this, so lye down the victim, close his nose while you breathe aie towards his mouth, if the chest arised, so you're doing great, keep repeating this")
    elif e.get() == "nausea and vomiting":
        myLabel = Label(root, text="Rest, keep hydrated taking small amounts of liquids all the time, prefer water, suck ice may really help,  don't stay a long time without eating, eat food like gelatine, biscuits cream-cracker and toasts, take metoclopramide and dimenhydrinate, if sever case with headache or bellyache seek medical service, if can't drink anything for 12 hours (adult) or 8 (children), vomiting taking more than 2 hours, feeling thirsty and with dry mouth, wakness, little urine flow or bloody vomit, thus seek help too")
    elif e.get() == "necessary medicines":
        myLabel = Label(root, text="if you want a first aid kit with medicines, you must have: anti-inflammatory, antacid, antiseptic sparay/Merthiolate, antispasmodic, antihistamine, painkiller, antipyretic, medicines for  nausea and vomiting and insect repelent; always note the expiry date")
    elif e.get() == "pesticides":
        myLabel = Label(root, text="if accidental INGESTION, seek medical help; if you think that some food has pesticides and you ate it, thus seek a hospital")
    elif e.get() == "rescue of the victim":
        myLabel = Label(root, text="if possible, use a rope or a ball; or be sure that you can swim until the victim and come back, involve his chest, passing through under one of his arms with your not dominant arm, keeping his face opposite to yours and swim with your dominant arm")
    elif e.get() == "seizure":
        myLabel = Label(root, text="Don't put anything inside the victim's mouth, don't try to take off anything from his mouth, protect him specially his head, lye him down, wait and then take victim to the hospital")
    elif e.get() == "sodium hydroxide and ammonia":
        myLabel = Label(root, text="if inhaled, stay at a ventilated place, while waiting for help, if it touched your skin, wash the region with water for 10 minutes")
    elif e.get() == "chlorine":
        myLabel = Label(root, text="If there was contact with skin or eyes, wash it for 10 minutes with only water, if ingested, drink water or a bit of olive oil and seek help")
    elif e.get() == "sodium hypochlorite":
        myLabel = Label(root, text="If there was contact with skin or eyes, wash it for 10 minutes with only water, if ingested, drink water or a bit of olive oil and seek help")
    elif e.get() == "sprain":
        myLabel = Label(root, text="apply ice enrolled in a thin tissue, hold it for between 15 and 20 minutes, if the skin turn to pale, gets tingling or weird, take off the ice, wait and start over, repeat it after each 2 hours for some days until the swelling and the pain disappear, don't apply heat to the region before the swelling disappears, never compress the injured region too hard, rest but not much (move the injured region sometimes), when lyed down raise the injured member and if you don't have diabetes, renal failure, gastritis nor duodenal ulcer, so take anti-inflammatories")
    elif e.get() == "sting":
        myLabel = Label(root, text="if SPIDER, apply a clean cloth and ice to the region; seek help immediatly if: fever, bubbles, skin daarkness, tachicardia, iintense sweat, seasickness, vomiting or anxiety;if SNAKE, take off compressing stuff from the body, apply ice, take dipyrone or paracetamol, if possible, also leave the species that atacked you to the hospitall, if DOMESTIC ANIMAL, wash the feriment with water and soap, cover it witha clean cloth or gauze and seek medical help, if SCORPIO, cover it with gauze and ice, take dipyrone or paracetamol and go to a hospital, meanly if the victim is a child, if there's somnolence, intense sweat, low blood pressure, tachicardia (palpitaion), seasickness or vomiting; if ANTS nad BEES, if there's breathing difficult or tachicardia, seek a hospital, if not grave, just apply ice in the injury")
    elif e.get() == "stroke":
        myLabel = Label(root, text="to know if a health problem is a stroke, say stroke symptoms; if it is, avoid calling an ambulance, use a car, taxi or ask for help and go to the nearest hospital really fast")
    elif e.get() == "stroke symptoms":
        myLabel = Label(root, text="tell the person to raise his arms, to sile and to speak; if he fails at doing one of these things or if he speaks weird and has muscle weakness, tingling, less movements or even fainting, so it's a stroke")
    elif e.get() == "transport wounded":
        myLabel = Label(root, text="if 2 lifeguards are available, so they must hold their arms forming a chair for  the victim to sit on and be carried:if 1 lifeguard, the victim must put his arm above and around your neck and you hold him or, if you can, raise him up with your both arms; IF the victim can't move and the way is long, put him above your shoullders with his legs  and one arm in  your front and the victim's back behind you, if the person may have injured his column, so avoid touching him and say fractures, looking for the word COLUMN")
    elif e.get() == "wild cassava":
        myLabel = Label(root, text="go to a hospital and say that your intoxication is due to wild cassava, because it releases CYANIDE, what may kill someone, don't ingest anythin while waiting")
# LABORATORY TESTS
    elif e.get() == "laboratory tests":
        myLabel = Label(root, text="choose a kind of laboratory test by saying: blood plasma serum, cerebrospinal fluid, hematologic, urine or pick up a specific one like: body mass index (or say bmi), sweat test about chloride levels, say chloride sweat, biochemical profile sma 12")
    elif e.get() == "17 hydroxycorticosteroids female":
        myLabel = Label(root, text="5.5 to 22 micromol per day or 2 to 8 miligrams per day")
    elif e.get() == "17 hydroxycorticosteroids male":
        myLabel = Label(root, text="8.2 to 27.6 micromol per day or 3 to 10 miligrams per day")
    elif e.get() == "17 ketosteroids female":
        myLabel = Label(root, text="21 to 52 micromol per day or 6 to 15 miligrams per day")
    elif e.get() == "17 ketosteroids male":
        myLabel = Label(root, text="28 to 70 micromol per day or 8 to 20 miligrams per day")
    elif e.get() == "alanine aminotransferase alt serum":
        myLabel = Label(root, text="8 to 20 units per liter")
    elif e.get() == "amylase serum":
        myLabel = Label(root, text="25 to 125 units per liter")
    elif e.get() == "aspartate aminotransferase ast serum":
        myLabel = Label(root, text="8 to 20 units per liter")
    elif e.get() == "bands":
        myLabel = Label(root, text="3 to 5%")
    elif e.get() == "basophils":
        myLabel = Label(root, text="0 to 0.75%")
    elif e.get() == "bicarbonate serum":
        myLabel = Label(root, text="22 to 28 milimol per liter or miliequivalent per liter")
    elif e.get() == "bilirubin serum adult direct":
        myLabel = Label(root, text="0 to 5 micromol per liter or 0 to 0.3 miligram per deciliter")
    elif e.get() == "bilirubin serum adult total":
        myLabel = Label(root, text="2 to 17 micromol per liter or 0.1 to 1 miligram per deciliter")
    elif e.get() == "blood plasma serum":
        myLabel = Label(root, text="choose from:, alanine aminotransferase alt serum, amylase serum, alanine aminotransferase ast serum, bilirubin serum adult total, bilirubin serum asdult direct, calcium serum, cholesterol serum, cortisol serum, creatine kinase serum male, creatine kinase serum female, creatinine serum, sodium serum, potassium serum, chloride serum, bicarbonate serum, magnesium serum, estriol in pregnancy serum 24 to 28 weeks, estriol in pregnancy serum 32 to 36 weeks, estriol in pregnancy serum 28 to 32 weeks, estriol in pregnancy serum 36 to 40 weeks, ferritin serum male, ferritin serum female, follicle stimulatin hormone serum male, follicle stimulatin hormone serum female, follicle stimulatin hormone serum midcycle peak, follicle stimulatin hormone serum postmenopause, ph arterial blood, pco2 arterial blood, po2 arterial blood, glucose serum fasting, glucose serum 2 hours postprandial, growth hormone arginine stimulation fasting, growth hormone arginine stimulation provocative stimuli, immunoglobulin iga serum, immunoglobulin ige serum, immunoglobulin igg serum, immunoglobulin igm serum, iron, lactate dehydrogenase serum, luteinizing hormone serum male, luteinizing hormone serum female, luteinizing hormone serum midcycle, luteinizing hormone serum postmenopause, osmolaity serum, parathyroid hormone serum n terminal, phosphstase alkaline serum p npp at 30 celsius degrees, phosphorus inorganic serum, prolactin serum hprl, total protein, protein albumin serum, protein globulin serum, thyroid stimulating hormone serum, thyroidal iodine uptake, thyroxine serum, triglycerides serum, triiodothyronine serum ria, triiodothyronine resin uptake, urea nitrogen serum, uric acid serum")
    elif e.get() == "body mass index":
        myLabel = Label(root, text="Result must be between 19 and 25 kilograms per meter squared")
    elif e.get() == "bmi":
        myLabel = Label(root, text="Result must be between 19 and 25 kilograms per meter squared")
    elif e.get() == "calcium":
        myLabel = Label(root, text="2.5 to 7.5 milimol per 25 hours or 100 to 300 miligrams per day")
    elif e.get() == "calcium serum":
        myLabel = Label(root, text="2.1 to 2.8 milimo per liter or 8.4 to 10.2 miligram per deciliter")
    elif e.get() == "cell count":
        myLabel = Label(root, text="0 to 5 mega per liter or 0 to 5 cubic milimeter")
    elif e.get() == "cerebrospinal fluid":
        myLabel = Label(root, text="choose from: cell count, chloride cerebrospinal, gamma globulin, glucose, pressure, proteins cerebrospinal")
    elif e.get() == "chloride cerebrospinal":
        myLabel = Label(root, text="118 to 132 milimol per liter or  miliequivalents per liter")
    elif e.get() == "chloride serum":
        myLabel = Label(root, text="95 to 105 milimol per liter or miliequivalent per liter")
    elif e.get() == "chloride sweat":
        myLabel = Label(root, text="Result must be between 0 and 45 milimol per liter")
    elif e.get() == "chloride urine":
        myLabel = Label(root, text="varies with intake")
    elif e.get() == "cholesterol serum":
        myLabel = Label(root, text="less than 5.2 milimol per liter or less than 200 miligram per deciliter")
    elif e.get() == "creatine kinase serum male":
        myLabel = Label(root, text="25 to 90 units per liter")
    elif e.get() == "creatine serum":
        myLabel = Label(root, text="53 to 106 micromol per liter or 0.6 to 1.2 miligram per deciliter")
    elif e.get() == "cortisol serum":
        myLabel = Label(root, text="800 hours: 138 to 635 nanomol per liter or 5 to 23 microgram per deciliter; 1600 hours: 82 to 413 nanomol per liter or 3 to 15 microgram per deciliter; 2000 hours; less than or equal to 50% of 800 hours")
    elif e.get() == "creatinine clearance male":
        myLabel = Label(root, text="97 to 137 mililiters per minute")
    elif e.get() == "eosinophils":
        myLabel = Label(root, text="1 to 3%")
    elif e.get() == "erythrocyte female":
        myLabel = Label(root, text="3.5 to 5.5 times 10 elevated to 12 per liter or 3.5 to 5.5 million per cubic milimeter")
    elif e.get() == "erythrocyte male":
        myLabel = Label(root, text="4.3 to 5.9 times 10 elevated to 12 per lter or 4.3 to 5.9 million per cubic milimeter")
    elif e.get() == "erythrocyte sedimentation rate westergren female":
        myLabel = Label(root, text="0 to 20 milimeter per hour")
    elif e.get() == "erythrocyte sedimentation rate westergren male":
        myLabel = Label(root, text="0 to 15 milimeter per hour")
    elif e.get() == "estriol in pregnancy serum 24 to 28 weeks":
        myLabel = Label(root, text="104 to 590 nanomol per liter or 30 to 170 nanogram per mililiter")
    elif e.get() == "estriol in pregnancy serum 28 to 32 weeks":
        myLabel = Label(root, text="140 to 760 nanomol per liter or 40 to 220 nanogram per mililiter")
    elif e.get() == "estriol in pregnancy serum 32 to 36 weeks":
        myLabel = Label(root, text="208 to 970 nanogram per liter or 60 to 280 nanogram per mililiter")
    elif e.get() == "estriol in pregnancy serum 36 to 40 weeks":
        myLabel = Label(root, text="280 to 1210 nanomol per liter or 80 to 350 nanogram per mililiter")
    elif e.get() == "estriol in pregnant 30 weeks":
        myLabel = Label(root, text="21 to 62 micromol per day or 6 to 18 miligrams per day")
    elif e.get() == "estriol in pregnant 35 weeks":
        myLabel = Label(root, text="31 to 97 micromol per day or 9 to 28 miligrams per day")
    elif e.get() == "estriol in pregnant 40 weeks":
        myLabel = Label(root, text="45 to 156 micromol per day or 13 to 42 miligrams per day")
    elif e.get() == "ferritin serum female":
        myLabel = Label(root, text="12 to 150 microgram per liter or nanogram per mililiter")
    elif e.get() == "ferritin serum male":
        myLabel = Label(root, text="15 to 200 microgram per liter or nanogram per liter")
    elif e.get() == "follicle stimulatin hormone serum female":
        myLabel = Label(root, text="4 to 30 units per liter")
    elif e.get() == "follicle stimulatin hormone serum male":
        myLabel = Label(root, text="4 to 25 units per liter")
    elif e.get() == "follicle stimulatin hormone serum midcyle peak":
        myLabel = Label(root, text="10 to 90 units per liter")
    elif e.get() == "follicle stimulatin hormone serum postmenopause":
        myLabel = Label(root, text="40 to 250 units per liter")
    elif e.get() == "gamma globulin":
        myLabel = Label(root, text="0.003 to 0.12 or 3 to 12 % of proteins")
    elif e.get() == "glucose":
        myLabel = Label(root, text="2.2 to 3.9 milimol per liter or 40 to 70 miligrams per deciliter")
    elif e.get() == "glucose serum 2 hours postprandial":
        myLabel = Label(root, text="less than 6.6 milimol per liter or less than 120 miligram per deciliter")
    elif e.get() == "glucose serum fasting":
        myLabel = Label(root, text="3.8 to 6.1 milimol per liter or 70 to 110 miligram per deciliter")
    elif e.get() == "growth hormone arginine fasting":
        myLabel = Label(root, text="less than 5 microgram per liter or nanogram per mililiter")
    elif e.get() == "growth hormone arginine stimulation provocative stimuli":
        myLabel = Label(root, text="more than 7 microgram per liter or nanogram pre mililiter")
    elif e.get() == "hematocrit female":
        myLabel = Label(root, text="36 to 46%")
    elif e.get() == "hematocrit male":
        myLabel = Label(root, text="41 to 53%")
    elif e.get() == "hematologic":
        myLabel = Label(root, text="choose from:, bleeding time, erythrocyte male, erythrocyte female, erythrocyte sedimentation rate westergren male, erythrocyte sedimentation rate westergren female, hematocrit male, hematocrit female, hemoglobin a, hemoglobin male, hemoglobin female, hemoglobin plasma, leukocyte count, segmented neutrophils, bands, eosinophils, basophils, lymphocytes, monocytes, mean corpuscular hemoglobin, mean corpuscular hemoglobin concentration, mean corpuscular volume, partial thromboplastin time activated, plateler count, phrothrombin time, reticulocyte count, thrombin time, plasma male, plasma female, red cell male, red cell female")
    elif e.get() == "hemoglobin a":
        myLabel = Label(root, text="less than or equal to 6%")
    elif e.get() == "hemoglobin female":
        myLabel = Label(root, text="1.86 to 2.48 milimol per liter or 12 to 16 grams per deciliter")
    elif e.get() == "hemoglobin male":
        myLabel = Label(root, text="2.09 to 2.71 milimol per liter or 13.5 to 17.5 grams per deciliter")
    elif e.get() == "hemoglobin plasma":
        myLabel = Label(root, text="0.16 to 0.62 milimol per liter or 1 to 4 miligram pre deciliter")
    elif e.get() == "immunoglobulin iga serum":
        myLabel = Label(root, text="0.76 to 3.9 grams per liter")
    elif e.get() == "immunoglobulin ige serum":
        myLabel = Label(root, text="0 to 380 kilounits per liter")
    elif e.get() == "immunoglobulin igg serum":
        myLabel = Label(root, text="6.5 to 15 gram per liter")
    elif e.get() == "immunoglobulin igm serum":
        myLabel = Label(root, text="0.4 to 3.45 grams per liter")
    elif e.get() == "intoxication and allergies":
        myLabel = Label(root, text="say pesticides, sodium hypochlorite(or just chlorine), food intoxication, gas, wild cassava, paracetamol, kerosene, cosmetics or sodium hydroxide and ammonia")
    elif e.get() == "iron":
        myLabel = Label(root, text="9 to 30 micromol per liter or 50 to 170 microgram per deciliter")
    elif e.get() == "kerosene":
        myLabel = Label(root, text="don't try to vomit, it could go to your lungs and worse things, go to a hospital")
    elif e.get() == "kidney stone":
        myLabel = Label(root, text="if you have renal colic, take an analgesic, antispasmodic or anti-inflamatory, if the pain doesn't get reduced, go to an emergency hospital, tell the employees that it'srenal colic and drink nothing")
    elif e.get() == "lactate dehydrogenase serum":
        myLabel = Label(root, text="45 to 90 units per liter")
    elif e.get() == "leukocyte count":
        myLabel = Label(root, text="4.5 to 11 times 10 elevated to 9 per liter or 4500 to 11000 per cubic milimeter")
    elif e.get() == "luteinizing hormone serum female":
        myLabel = Label(root, text="5 to 30 units per liter")
    elif e.get() == "luteinizing hormone serum male":
        myLabel = Label(root, text="6 to 23 units per liter")
    elif e.get() == "luteinizing hormone serum midcycle":
        myLabel = Label(root, text="75 to 150 units per liter")
    elif e.get() == "luteinizng hormone serum postmenopause":
        myLabel = Label(root, text="30 to 200 units")
    elif e.get() == "lymphocytes":
        myLabel = Label(root, text="25 to 33%")
    elif e.get() == "magnesium serum":
        myLabel = Label(root, text="0.75 to 1 milimol per liter or 1.5 to 2 miliequivalent per liter")
    elif e.get() == "mean corpuscular hemoglobin":
        myLabel = Label(root, text="0.39 to 0.54 fmol per cell or 25.4 to 34.6 pg per cell")
    elif e.get() == "mean corpuscular hemoglobin concentration":
        myLabel = Label(root, text="4.81 to 5.58 milimol Hb per liter or 31 to 36% Hb per cell")
    elif e.get() == "mean corpuscular volume":
        myLabel = Label(root, text="80 to 100 f liter or cubic micrometer")
    elif e.get() == "monocytes":
        myLabel = Label(root, text="3 to 7%")
    elif e.get() == "osmolality":
        myLabel = Label(root, text="50 to 1400 miliosmol per kilogram of water")
    elif e.get() == "osmolality serum":
        myLabel = Label(root, text="275 to 295 miliosmol per kilogram of water")
    elif e.get() == "oxalate":
        myLabel = Label(root, text="90 to 445 micromol per liter or 8 to 40 micrograms per mililiter")
    elif e.get() == "paracetamol":
        myLabel = Label(root, text="try to remember the amount of pills ingested, try to vomit them and take N-acetylcyateine, dissolving it into water, if it desn't work seek medical service")
    elif e.get() == "parathyroid hormone serum n terminal":
        myLabel = Label(root, text="230 to 630 nanogram per liter")
    elif e.get() == "partial thromboplastin time activated":
        myLabel = Label(root, text="25 to 40 seconds")
    elif e.get() == "pco2 arterial blood":
        myLabel = Label(root, text="4.4 to 5.9 kilopascal or 33 to 45 milimeter of mercury")
    elif e.get() == "ph arterial boold":
        myLabel = Label(root, text="36 to 44 nanomol per liter of protons or 7.35 to 7.45")
    elif e.get() == "phosphatase alkaline serum p npp at 30 celsius degrees":
        myLabel = Label(root, text="20 to 70 units per liter")
    elif e.get() == "phosphorus inorganic serum":
        myLabel = Label(root, text="1 to 1.5 milimol per liter or 3 to 4.5 miligram per deciliter")
    elif e.get() == "plasma female":
        myLabel = Label(root, text="0.028 to 0.045 liter per kilogram")
    elif e.get() == "plasma male":
        myLabel = Label(root, text="0.025 to 0.043 liter per kilogram")
    elif e.get() == "platelet count":
        myLabel = Label(root, text="150 to 400 times elevated to 9 per liter or 150000 to 400000 per cubic milimeter")
    elif e.get() == "po2 arterial blood":
        myLabel = Label(root, text="10 to 14 kilopascal or 75 to 105 milimeter of mercury")
    elif e.get() == "potassium":
        myLabel = Label(root, text="varies with diet")
    elif e.get() == "potassium serum":
        myLabel = Label(root, text="3.5 to 5 milimol perliter or miliequivalent per liter")
    elif e.get() == "pressure":
        myLabel = Label(root, text="70 to 180 milimeter of water")
    elif e.get() == "prolactin serum hprl":
        myLabel = Label(root, text="less than 20 microgram per liter")
    elif e.get() == "protein albumin serum":
        myLabel = Label(root, text="35 to 55 gram per liter")
    elif e.get() == "protein globulin serum":
        myLabel = Label(root, text="23 to 35 grams per liter")
    elif e.get() == "proteins cerebrospinal":
        myLabel = Label(root, text="less than 0.4 gram per liter")
    elif e.get() == "proteins urine":
        myLabel = Label(root, text="less than 0.15 grams per day")
    elif e.get() == "prothrombin time":
        myLabel = Label(root, text="11 to 15 seconds")
    elif e.get() == "red cell female":
        myLabel = Label(root, text="0.019 to 0.031 liter per kilogram")
    elif e.get() == "red cell male":
        myLabel = Label(root, text="0.02 to 0.036 liter per kilogram")
    elif e.get() == "reticulocyte count":
        myLabel = Label(root, text="0.5 to 1.5%")
    elif e.get() == "segmented neutrophils":
        myLabel = Label(root, text="54 to 62%")
    elif e.get() == "sodium":
        myLabel = Label(root, text="varies with diet")
    elif e.get() == "sodium serum":
        myLabel = Label(root, text="136 to 145 milimol per liter or miliequivalent per liter")
    elif e.get() == "thrombin time":
        myLabel = Label(root, text="less than 2 seconds deviation from control")
    elif e.get() == "thyroid stimulating hormone serum":
        myLabel = Label(root, text="0.5 to 5 miliunits per liter")
    elif e.get() == "thyroidal iodine uptake":
        myLabel = Label(root, text="8 to 30 % of adminitered dose of 123Iode (isotope) per day")
    elif e.get() == "thyroxine serum":
        myLabel = Label(root, text="About T4: 64 to 155 nanomol per liter or 5 to 12 microgram per deciliter")
    elif e.get() == "total protein":
        myLabel = Label(root, text="60 to 78 grams per liter")
    elif e.get() == "triglycerides serum":
        myLabel = Label(root, text="0.4 to 1.81 milimol per liter or 35 to 160 miligram per deciliter")
    elif e.get() == "triiodothyronine resin uptake":
        myLabel = Label(root, text="About T3: 25 to 35%")
    elif e.get() == "triiodothyronine serum ria":
        myLabel = Label(root, text="About T3: 1.8 to 2.9 nanomol per liter or 115 to 190 nanogram per deciliter")
    elif e.get() == "urea nitrogen serum":
        myLabel = Label(root, text="1.2 to 3 milimol per liter or 7 to 18 miligram per deciliter")
    elif e.get() == "uric acid":
        myLabel = Label(root, text="varies with diet")
    elif e.get() == "uric acid serum":
        myLabel = Label(root, text="0.1 to 0.48 milimol per liter or 3 to 8.2 miligram per deciliter")
    elif e.get() == "urine":
        myLabel = Label(root, text="choose from: calcium, chloride urine, creatinine clearance male, creatinine clearance female, estriol in pregnant 30 weeks, estriol in pregnant 35 weeks, estriol in pregnant 40 weeks, 17 hydroxycorticosteroids male, 17 hydroxycorticosteroids female, 17 ketosteroids male, 17 ketosteroids female, osmolality, oxalate, potassium, proteins urine, sodium, uric acid")
# RARE ISSUES
    elif e.get() == "immortal":
        myLabel = Label(root, text="say treatment aging, say poisons, have a plant based diet (you can eat low fat proteins sometimes), meditate (or get hypnotized), provocate hyperthermia willinly, drink EZ (exclusion zone) and alcaline water, aspirin increases EZ water, take soda only sometimes; every day, take a lot of care of your body, exercise well, manage well your sleep and your stress, care about your safety and prevention of diseases and do everything I tell you to do")
    elif e.get() == "immortality":
        myLabel = Label(root, text="say treatment aging, say poisons, have a plant based diet (you can eat low fat proteins sometimes), meditate (or get hypnotized), provocate hyperthermia willinly, drink EZ (exclusion zone) and alcaline water, aspirin increases EZ water, take soda only sometimes; every day, take a lot of care of your body, exercise well, manage well your sleep and your stress, care about your safety and prevention of diseases and do everything I tell you to do")
    elif e.get() == "treatment aging":
        myLabel = Label(root, text="take 8 to 12 mg of cycloastragenol per day, take herbs, teas, a little bit of all foods, very little amount of fat and candies, exercise, sleep at least a little, have some fun, do stuff for yourself, avoid stressful people (it's better to be alone), take only a little ssunlight and enjoy your time: work a lot, study a lot, have a lot of fun and love when find a worthy woman")
    elif e.get() == "poisons":
        myLabel = Label(root, text="Never take chemotheraphy, claimed anti-aids drugs, vaccine, NSAIDS and drugs in general, prefer herbs and teas; don't take fluoride, chlorine water, thimerosol (has ethil mercury), deodorant, animal fat (may contain dioxins, including milk fat), don't eat fish fat (mercury), industrialized cheese ...")
    elif e.get() == "diagnosis farting":
        myLabel = Label(root, text="diagnosis is disbiosis, this is, excess of bad gut bacteria or diagnosis is rigid belly")
    elif e.get() == "treatment disbiosis":
        myLabel = Label(root, text="Persist in the pooping until your belly gets empty, persist more, more and More! Take some fermented milk with Lactobacillus; if advanced condition, take 7 litters in two followed days (Friday at night)")
    elif e.get() == "treatment migraine":
        myLabel = Label(root, text="sleep, relax or take enerumab; to relieve a postspinal tap headache, apply pressue on both jugular veins")
    elif e.get() == "treatment rigid belly":
        myLabel = Label(root, text="elongate daily all your abdominal wall in evry possible way, this will turn your belly more flexible, allowing your intestines to store a bigger volume")
    elif e.get() == "treatment aids":
        myLabel = Label(root, text="at first, never take claimed anti-aids drugs such as AZT, Retrovir etc, those are poisons:do a bone marrow transplant from someone with the 32 mutation")
    elif e.get() == "treatment hiv":
        myLabel = Label(root, text="at first, never take claimed anti-aids drugs such as AZT, Retrovir etc, those are poisons:do a bone marrow transplant from someone with the 32 mutation")
    elif e.get() == "treatment cancer":
        myLabel = Label(root, text="take dichloroacetate (DCA) or PDK siRNA inhibitor (it mimics DCA), take iodine, apply the none carbohydrate diet (you can eat proteins and a little of fat until the cancer disappears), take amygdalin and phosphoetanolamine, the one made by Gilberto Chierice, the Sao Paulo University professor")
    elif e.get() == "treatment carcinome":
        myLabel = Label(root, text="take dichloroacetate (DCA) or PDK siRNA inhibitor (it mimics DCA), take iodine, apply the none carbohydrate diet (you can eat proteins and a little of fat until the cancer disappears), take amygdalin and phosphoetanolamine, the one made by Gilberto Chierice, the Sao Paulo University professor")
# DISEASES TESTS
    elif e.get() == "tests cholecystitis and Rovsing’s sign in appendicitis":
        myLabel = Label(root, text="look for Murphy’s sign")
    elif e.get() == "tests diverticulitis of the sigmoid colon":
        myLabel = Label(root, text="look for reverse Rovsing’s sign")
    elif e.get() == "tests tender adnexal mass":
        myLabel = Label(root, text="look for pelvic inflammatory disease, ectopic pregnancy and inflamed pelvic appendix")
    elif e.get() == "tests ectopic pregnancy":
        myLabel = Label(root, text="look for amenorrhea, morning sickness, and tender breasts")
    elif e.get() == "tests pelvic inflammatory disease":
        myLabel = Label(root, text="look for a vaginal discharge")
    elif e.get() == "tests retracted right testicle":
        myLabel = Label(root, text="look for appendicitis")
    elif e.get() == "tests retracted left testicle":
        myLabel = Label(root, text="look for diverticulitis")
    elif e.get() == "tests retracted testicles":
        myLabel = Label(root, text="look for peritonitis")
    elif e.get() == "tests gross blood in rectal examination":
        myLabel = Label(root, text="look for intussusception and mesenteric thrombosis")
    elif e.get() == "tests occult blood in rectal examination":
        myLabel = Label(root, text="look for peptic ulcer disease, diverticulitis, and carcinoma of the bowel")
    elif e.get() == "tests costochondritis":
        myLabel = Label(root, text="palpate the costochondral junctions at the second, third and fourth ribs")
    elif e.get() == "tests rib fracture":
        myLabel = Label(root, text="palpate the ribs")
    elif e.get() == "tests pneumothorax by tracheal deviation":
        myLabel = Label(root, text="lungs auscultation")
    elif e.get() == "tests pulmonary embolism":
        myLabel = Label(root, text="lungs auscultation")
    elif e.get() == "pneumonia with pleurisy":
        myLabel = Label(root, text="lungs auscultation")
    elif e.get() == "tests reflux esophagitis":
        myLabel = Label(root, text="reproduce the pain with pressure in the mid-epigastrium or relief it with a swallow of 5 to 10 mililiter of lidocaine viscous")
    elif e.get() == "tests hyperthyroidism":
        myLabel = Label(root, text="look for tremor, tachycardia and thyroid mass")
    elif e.get() == "tests ear, nose and throat examination":
        myLabel = Label(root, text="if normal, so you can exclude impacted cerumen, foreign body, otitis media and cholesteatoma")
    elif e.get() == "tests whisper":
        myLabel = Label(root, text="do it at 2 meters away with each ear, if normal, then exclude Meniere's disease and acoustic neuroma; if in doubt, so refer the pacient for an audiogram: Weber and Rinne's tests can help determine whether you have a vertigo from a middle ear disorder (Meniere's disease) or inner ear with nerve damage (acoustic neuroma)")
    elif e.get() == "tests acute sinusitis":
        myLabel = Label(root, text="one or more sinuses may fail to transilluminate")
    elif e.get() == "McMurray’s test":
        myLabel = Label(root, text="do this to detect torn meniscus")
    elif e.get() == "tests Lachman’s maneuver":
        myLabel = Label(root, text="do this to detect anterior cruciate ligament tear")
    elif e.get() == "tests cholecystitis":
        myLabel = Label(root, text="if there are abdominal pain, nausea, vomiting and a shoulder ache, thus diagnosis is cholecystitis")
    elif e.get() == "tests pneumonia":
        myLabel = Label(root, text="if there are sputum smear and culture and agreeing chest x-ray, therefore diagnosis is pneumonia")
    elif e.get() == "tests myocardial infarction":
        myLabel = Label(root, text="if he electrocardiogram, serial and cardiac enzymes tests agree, so diagnosis is myocardial infarction")
# ANESTHESIOLOGY
# CARDIOLOGY
    elif e.get() == "diagnosis chest pain":
        myLabel = Label(root, text="cite the location, by saying: left precardium, pain by inspiration, pain by extenson or rotation of the spine, acute chest pain, chronic or recurring chest pain, chest pain radiating to the neck, jaw or left upper extremity, chest pain with diaphoresis, chest pain with hemoptysis, chest pain with regurgitation of food or acid, chest pain with rash")
    elif e.get() == "left precardium":
        myLabel = Label(root, text="consider myocardial insufficiency, infarct, pericarditis etc")
    elif e.get() == "pain by inspiration":
        myLabel = Label(root, text="consider pleurisy, costochondritis, pulmonary embolism, rib fractures, reflux esophagitis etc")
    elif e.get() == "pain by extenson or rotation of the spine":
        myLabel = Label(root, text="consider vertebral fracture, herniated disk etc")
    elif e.get() == "acute chest pain":
        myLabel = Label(root, text="consider pulmonary embolism, pneumothorax, pneumonia with pleurisy, fractures, costochondritis or myocardial infarction")
    elif e.get() == "chronic or recurring chest pain":
        myLabel = Label(root, text="consider coronary insufficiency, reflux esophagitis, thoracic spondylosis etc")
    elif e.get() == "chest pain radiating to the neck, jaw or left upper extremity":
        myLabel = Label(root, text="consider myocardial infarction and coronary insufficiency")
    elif e.get() == "chest pain with diaphoresis":
        myLabel = Label(root, text="consider myocardial infarction and pulmonary embolism")
    elif e.get() == "chest pain with hemoptysis":
        myLabel = Label(root, text="consider pulmonary embolism")
    elif e.get() == "chest pain with regurgitation of food or acid":
        myLabel = Label(root, text="consider reflux esophagitis")
    elif e.get() == "chest pain with rash":
        myLabel = Label(root, text="consider herpes zoster")
    elif e.get() == "Hallpike maneuvers":
        myLabel = Label(root, text="With the pacient sitting sideways on the exam table, turn his orher head to the right and quiclky lower the head and torso so that the head is below the edge of the table and observe for nystagmus or vertigo for at least 2 to 3 minutes.\nThen, raise the pacients head and torso back  to the upright position and again observe for nystagmus or vertigo. Repeat the same procedure with the pacient's head straight and turned to the left.\nIf the pacient experiences vertigo or you observe nystagmus in one of these positions, then a diagnosis of benign positional vertigo is likely.\nWith other form of vertigo, you may precipitate the sensation in many of these positions or vertigo will not be precipitated at all.")
# DERMATOLOGY
# EMERGENCY
# ENDOCRINOLOGY
# GASTROENTEROLOGY
    elif e.get() == "diagnosis abdominal pain":
        myLabel = Label(root, text="say diagnosis acute abdominal pain or diagnosis farting")
    elif e.get() == "diagnosis acute abdominal pain":
        myLabel = Label(root, text="say the location and type of the pain: right upper quadrant, epigastric, right lower quadrant, left lower quadrant, diffuse abdominal pain or severe abdominal pain; then say: constant abdominal pain or intermittent abdominal pain and say meals associated abdominal pain. Then, check out the confirmative tests of the diseases which appear the most in this questionnaire")
    elif e.get() == "right upper quadrant":
        myLabel = Label(root, text="consider cholecystitis or duodenal ulcer")
    elif e.get() == "epigastric":
        myLabel = Label(root, text="consider pancreatitis, gastric ulcer, reflux esophagitis, and myocardial infarction")
    elif e.get() == "right lower quadrant":
        myLabel = Label(root, text="consider appendicitis, ectopic pregnancy and pelvic inflammatory disease")
    elif e.get() == "left lower quadrant":
        myLabel = Label(root, text="consider diverticulitis, ectopic pregnancy, and pelvic inflammatory disease")
    elif e.get() == "diffuse abdominal pain":
        myLabel = Label(root, text="consider diverticulitis, ectopic pregnancy, and pelvic inflammatory disease")
    elif e.get() == "severe abdominal pain":
        myLabel = Label(root, text="consider acute pancreatitis, ruptured viscus, biliary colic or renal colic")
    elif e.get() == "constant abdominal pain":
        myLabel = Label(root, text="consider cholecystitis, appendicitis, diverticulitis, etc")
    elif e.get() == "intermittent abdominal pain":
        myLabel = Label(root, text="consider biliary colic, renal colic, intestinal obstruction")
    elif e.get() == "meals associated abdominal pain":
        myLabel = Label(root, text="pain occurring 1 to 2 hours after meals might be peptic ulcer or reflux, pain occurring 2 to 3hours after meals might indicate cholecystitis or cholelithiasis")
    elif e.get() == "diagnosis diarrhea, nausea, vomiting":
        myLabel = Label(root, text="diagnosis is gastroenteritis")
    elif e.get() == "diagnosis fever, loss of apetite, mild nausea":
        myLabel = Label(root, text="diagnosis is appendicitis")
    elif e.get() == "diagnosis nausea, vomiting":
        myLabel = Label(root, text="diagnosis is cholecystitis, intestinal obstruction, pancreatitis or renal colic")
    elif e.get() == "diagnosis severe nausea, vomiting":
        myLabel = Label(root, text="diagnosis is cholecystitis, intestinal obstruction, pancreatitis or renal colic")
    elif e.get() == "diagnosis diaphoresis, history of diabetes, hyperlipemia or hypertension":
        myLabel = Label(root, text="diagnosis is myocardial infarction")
    elif e.get() == "diagnosis history of diabetes, hyperlipemia or hypertension, severe diaphoresis":
        myLabel = Label(root, text="diagnosis is myocardial infarction")
    elif e.get() == "diagnosis history of alcoholism":
        myLabel = Label(root, text="diagnosis is acute pancreatitis")
    elif e.get() == "diagnosis recurrent regurgitation of food or acid":
        myLabel = Label(root, text="diagnosis is reflux esophagitis")
    elif e.get() == "diagnosis rebound tenderness in the right upper quadrant":
        myLabel = Label(root, text="diagnosis is cholecystitis")
    elif e.get() == "diagnosis rebound tenderness in the right lower quadrant":
        myLabel = Label(root, text="diagnosis is appendicitis")
    elif e.get() == "diagnosis rebound tenderness in the left lower quadrant":
        myLabel = Label(root, text="diagnosis is diverticulitis")
    elif e.get() == "diagnosis rebound tenderness":
        myLabel = Label(root, text="say diffuse rebound tenderness, diagnosis is pelvic inflammatory disease, ectopic pregnancy or say: rebound tenderness in the X quadrant")
    elif e.get() == "diagnosis diffuse rebound tenderness":
        myLabel = Label(root, text="diagnosis is pancreatitis or ruptured viscus, ruptured peptic ulcer or peritonitis")
    elif e.get() == "diagnosis tender mass in the right upper quadrant":
        myLabel = Label(root, text="diagnosis is cholecystitis or hepatitis")
    elif e.get() == "diagnosis tender mass in the right lower quadrant":
        myLabel = Label(root, text="diagnosis is a ruptured appendix")
    elif e.get() == "diagnosis mass in the groin":
        myLabel = Label(root, text="diagnosis is intestinal obstruction")
    elif e.get() == "diagnosis mass in the umbilicus":
        myLabel = Label(root, text="diagnosis is intestinal obstruction")
    elif e.get() == "diagnosis umbilical hernia":
        myLabel = Label(root, text="diagnosis is intestinal obstruction")
    elif e.get() == "diagnosis icteric sclera":
        myLabel = Label(root, text="diagnosis is cholecystitis or hepatitis")
    elif e.get() == "diagnosis hyperactive bowel sounds":
        myLabel = Label(root, text="diagnosis is intestinal obstruction")
    elif e.get() == "noisy bowel":
        myLabel = Label(root, text="diagnosis is intestinal obstruction")
    elif e.get() == "diagnosis decreased bowel sounds":
        myLabel = Label(root, text="diagnosis is peritonitis or ruptured viscus")
    elif e.get() == "diagnosis regurgitation of acid or food":
        myLabel = Label(root, text="diagnosis is reflux esophagitis")
    elif e.get() == "treatment reflux esophagitis":
        myLabel = Label(root, text="take 5 to 10 mililiter of lidocaine viscous")
    elif e.get() == "diagnosis diarrhea":
        myLabel = Label(root, text="say: acute diarrhea, chronic diarrhea, taken antibiotics diarrhea, taken drugs diarrhea, bloody diarrhea, diabetes mellitus diarrhea, aids diarrhea, out of the country diarrhea, weight loss diarrhea, floating stools diarrhea, flushing diarrhea, peptic ulcers diarrhea, milk intolerance diarrhea and look for tests hyperthyroidism, rash diarrhea, peripheral neuropathy diarrhea, abdominal mass diarrhea")
    elif e.get() == "acute diarrhea":
        myLabel = Label(root, text="consider viral, bacterial, staphylococcal, toxins")
    elif e.get() == "chronic diarrhea":
        myLabel = Label(root, text="consider lactose intolerance, inflammatory bowel disease, carcinoid, Zollinger–Ellison syndrome, irritable bowel etc")
    elif e.get() == "diagnosis diarrhea, nausea, vomiting":
        myLabel = Label(root, text="diagnosis is viral gastroenteritis")
    elif e.get() == "diagnosis chills, diarrhea, fever":
        myLabel = Label(root, text="diagnosis is bacterial gastroenteritis")
    elif e.get() == "taken antibiotics diarrhea":
        myLabel = Label(root, text="consider C. difficile toxin")
    elif e.get() == "taken drugs diarrhea":
        myLabel = Label(root, text="consider toxic diarrhea")
    elif e.get() == "bloody diarrhea":
        myLabel = Label(root, text="consider (inflammatory bowel disease, bacterial gastroenteritis, ischemic colitis and neoplasm")
    elif e.get() == "diabetes mellitus diarrhea":
        myLabel = Label(root, text="consider diabetic enteropathy")
    elif e.get() == "aids diarrhea":
        myLabel = Label(root, text="consider C. parvum")
    elif e.get() == "out of the country diarrhea":
        myLabel = Label(root, text="consider Escherichia coli")
    elif e.get() == "weight loss diarrhea":
        myLabel = Label(root, text="consider neoplasm, hyperthyroidism and malabsorption syndrome")
    elif e.get() == "floating stools diarrhea":
        myLabel = Label(root, text="consider malabsorption syndrome")
    elif e.get() == "flushing diarrhea":
        myLabel = Label(root, text="consider carcinoid syndrome")
    elif e.get() == "peptic ulcers diarrhea":
        myLabel = Label(root, text="consider Zollinger–Ellison syndrome")
    elif e.get() == "milk intolerance diarrhea":
        myLabel = Label(root, text="consider lactose intolerance")
    elif e.get() == "rash diarrhea":
        myLabel = Label(root, text="consider pellagra, carcinoid syndrome and inflammatory bowel disease")
    elif e.get() == "peripheral neuropathy diarrhea":
        myLabel = Label(root, text="consider diabetic enteropathy, pellagra etc")
    elif e.get() == "abdominal mass diarrhea":
        myLabel = Label(root, text="consider neoplasm and inflammatory disease")
    elif e.get() == "diagnosis rectal bleeding":
        myLabel = Label(root, text="say: pain on defecation rectal bleeding, painless rectal bleeding, bloody stools rectal bleeding, diarrhea rectal bleeding, intestinal obstruction rectal bleeding, ecchyomosis or bleeding elsewhere rectal bleeding; do rectal and anoscopic examinations in the pacients with acute rectal bleeding with no diarrhea nor evidence of instestinal obstruction; do an inspection to detect hemorrhoids; do a sentinel pile to an anal fissure, which usually occurs at 6 o'clock; do anoscopic and proctoscopic examinations to detect rectal carcinomas, internal hemorrhoids and anal fissures (when inspection and palpation can't identify them)")
    elif e.get() == "pain on defecation rectal bleeding":
        myLabel = Label(root, text="consider thrombosed hemorrhoids and anal fissure")
    elif e.get() == "painless rectal bleeding":
        myLabel = Label(root, text="consider carcinoma and internal or external hemorrhoids without thrombosis")
    elif e.get() == "bloody stools rectal bleeding":
        myLabel = Label(root, text="consider colon neoplasm and diverticulitis")
    elif e.get() == "diarrhea rectal bleeding":
        myLabel = Label(root, text="consider ulcerative colitis, Crohn's disease and amebic dysentery")
    elif e.get() == "intestinal obstruction rectal bleeding":
        myLabel = Label(root, text="consider intussusception and mesenteric thrombosis")
    elif e.get() == "ecchyomosis or bleeding elsewhere rectal bleeding":
        myLabel = Label(root, text="diagnosis is coagulation disorder")
    elif e.get() == "abdominal acute pain":
        myLabel = Label(root, text="say extra-abdominal or abdominal")
    elif e.get() == "extra-abdominal":
        myLabel = Label(root, text="say sweet breath, productive cough, shock and shortness of breath, family or personal history of epilepsy or migraine, black ancestry or black widow spider bite")
    elif e.get() == "sweet breath":
        myLabel = Label(root, text="diagnosis is diabetic acidosis")
    elif e.get() == "productive cough":
        myLabel = Label(root, text="say tests pneumonia")
    elif e.get() == "shock and shortness of breath":
        myLabel = Label(root, text="say tests myocardial infarction")
    elif e.get() == "family or personal history of epilepsy or migraine":
        myLabel = Label(root, text="use electroencephalography to differentiate between epilepsy, migraine and anemia")
    elif e.get() == "black ancestry":
        myLabel = Label(root, text="use sickle cell prep to confirm diagnosis of sickle cell")
    elif e.get() == "black widow spider bite":
        myLabel = Label(root, text="diagnosis is black widow spider bite")
    elif e.get() == "abdominal":
        myLabel = Label(root, text="say intermittent colicky pain or persistent pain")
    elif e.get() == "intermittent colicky pain":
        myLabel = Label(root, text="say hyperactive bowel sounds, tympany; right upper quadrant, slight jaundice or dark urine; flank, hematuria")
    elif e.get() == "hyperactive bowel sounds, tympany":
        myLabel = Label(root, text="if there is flat plate of abdomen, so diagnosis is intestinal obstruction")
    elif e.get() == "right upper quadrant, slight jaundice or dark urine":
        myLabel = Label(root, text="use ultrasound of gallbladder and hida scan to differentiate between cholelithiasis and choledocholithiasis")
    elif e.get() == "flank, hematuria":
        myLabel = Label(root, text="if there are agreeing intravenous pyelogram and ct scan, so diagnosis is nephrolithiasis")
    elif e.get() == "persistent pain":
        myLabel = Label(root, text="say generalized with rebound tenderness or focal tenderness and rebound")
    elif e.get() == "generalized with rebound tenderness":
        myLabel = Label(root, text="say board-like ridigity, shock or bloody stool")
    elif e.get() == "board-like ridigity":
        myLabel = Label(root, text="if there are flat plate of the abdomen and upright plate for free air under diaphrgm, so diagnosis is perforated ulcer")
    elif e.get() == "shock":
        myLabel = Label(root, text="if there is agreeing serum amylase test, thus diagnosis is acute pancreatitis")
    elif e.get() == "bloody stool":
        myLabel = Label(root, text="use a ct scan do differentiate between mesenteric thrombosis, mesenteric embolism and intussusception")
    elif e.get() == "abdominal pain chronic recurrent":
        myLabel = Label(root, text="say family history or epilepsy or migraine; no family history or epislepsy or migraine")
    elif e.get() == "family history or epilepsy or migraine":
        myLabel = Label(root, text="thus, diagnosis is epilepsy or migraine")
    elif e.get() == "no family history or epilepsy or migraine":
        myLabel = Label(root, text="say colicky; persistent")
    elif e.get() == "colicky":
        myLabel = Label(root, text="say flank pain, midabdominal; ruqrs")
    elif e.get() == "flank pain":
        myLabel = Label(root, text="if there is flank pain, so test for radiation to testicle to diagnose renal calculus")
    elif e.get() == "midabdominal":
        myLabel = Label(root, text="if there is midabdominal pain, therefore diagnosis is partial intestinal obstruction")
    elif e.get() == "ruqrs":
        myLabel = Label(root, text="if there is right upper quadrant pain radiating to shoulder, so diagnosis is cholelithiasis")
    elif e.get() == "persistent":
        myLabel = Label(root, text="say localized; not localized")
    elif e.get() == "localized":
        myLabel = Label(root, text="say upper abdomen, flank, lower abdomen")
    elif e.get() == "upper abdomen":
        myLabel = Label(root, text="say ajrrs, relieved by food, history of alcoholism")
    elif e.get() == "ajrrs":
        myLabel = Label(root, text="if there is pain associated with jaundice radiating to right scapule, thus diagnosis is cholelithiasis")
    elif e.get() == "relieved by food":
        myLabel = Label(root, text="if pain is relieved by food, so diagnosis is peptic ulcer")
    elif e.get() == "history of alcoholism":
        myLabel = Label(root, text="if there is history of alcoholism, so diagnosis is chronic pancreatitis")
    elif e.get() == "flank":
        myLabel = Label(root, text="if there is flank pain, therefore diagnosis is pyelonephritis")
    elif e.get() == "lower abdomen":
        myLabel = Label(root, text="say right ap, midhypogastrium, left ap")
    elif e.get() == "right ap":
        myLabel = Label(root, text="if there is a right pain, thus diagnosis is regional ileitis, salpingitis or endometriosis")
    elif e.get() == "midhypogastrium":
        myLabel = Label(root, text="if there is midhypogastrium pain, so diagnosis is chronic cystitis, bladder calculus, bladder neck obstruction, pelvic inflammatory disease or pelvic appendix")
    elif e.get() == "left ap":
        myLabel = Label(root, text="if there is left pain, so diagnosis is diverticulitis, salpingitis or endometriosis")
    elif e.get() == "not localized":
        myLabel = Label(root, text="if the pain is not localized, therefore diagnosis is irritable bowel syndrome, paralytic ileus or peritonitis")
    elif e.get() == "abdominal rigidity":
        myLabel = Label(root, text="if there are tenderness and rebound tenderness, so say absent; present")
    elif e.get() == "absent":
        myLabel = Label(root, text="if there is absent ridigity, so diagnosis is voluntary rigidity")
    elif e.get() == "present":
        myLabel = Label(root, text="if there is present ridigity, thus say present ht; absent ht")
    elif e.get() == "present ht":
        myLabel = Label(root, text="if there is presence of history of trauma, so diagnosis is ruptured spleen, other abdominal organ rupture or damage")
    elif e.get() == "absent ht":
        myLabel = Label(root, text="if there is absent ridigity, so say present hrap; absent hrap")
    elif e.get() == "present hrap":
        myLabel = Label(root, text="if there is present history of recurrent abdominal pain, so diagnosis is ruptured peptic ulcer, ruptured diverticulum or perforated gall bladder")
    elif e.get() == "absent hrap":
        myLabel = Label(root, text="if there is absent history of recurrent abdominal pain, thus diagnosis is lobar pneumonia, ruptured appendix, pid, black widow spider bite, ruptured ectopic pregnancy, infectious peritonitis, pancreatitis, mesenteric thrombosis dissecting aneurysm, etc")
    elif e.get() == "abdominal swelling focal":
        myLabel = Label(root, text="say upper asf; lower asf")
    elif e.get() == "upper asf":
        myLabel = Label(root, text="say right asf; epigastrium; left asf")
    elif e.get() == "right asf":
        myLabel = Label(root, text="say tender asf; nontender asf")
    elif e.get() == "tender asf":
        myLabel = Label(root, text="so diagnosis is liver in hepatitis and congestive heart failure, gallbladder in cholecystiis, subphrenic abscess, perinephric abscess, tumor of colon or abdominal wall hematoma")
    elif e.get() == "nontender asf":
        myLabel = Label(root, text="thus diagnosis is hepatomegaly renal tumor, adrenal tumor, courvoisier gallbladder, hydrops of gallbladder or fecal impaction")
    elif e.get() == "epigastrium":
        myLabel = Label(root, text="therefore diagnosis is omental hernia, pancreatic tumor, pancreatic cyst, gastric carcinoma, pyloric stenosis, aortic aneurysm, retroperitoneal sarcoma or hepatomegaly")
    elif e.get() == "left asf":
        myLabel = Label(root, text="so diagnosis is splenomegaly abdominal wall hematoma, pancreatic tumor, pancreatic cyst, gastric tumor, colon tumor, kidney tumor or enlargement or fecal impaction")
    elif e.get() == "lower asf":
        myLabel = Label(root, text="say right l, hypogastrium l, left l")
    elif e.get() == "right l":
        myLabel = Label(root, text="say tender right l, nontender right l")
    elif e.get() == "tender right l":
        myLabel = Label(root, text="diagnosis is appendiceal abscess, psoas abscess, pyosalpinx, regional ileitis or intussusception")
    elif e.get() == "nontender right l":
        myLabel = Label(root, text="diagnosis is carcinoma of the colon or ovarian tumor")
    elif e.get() == "hypogastrium l":
        myLabel = Label(root, text="diagnosis is bladder, pregnant uterus, uterine fibroids, regional, ileitis or urachal cyst")
    elif e.get() == "left l":
        myLabel = Label(root, text="diagnosis is sigmoid colon, diverticulitis, carcinoma of the colon, ovarian tumor or pyosalpinx")
    elif e.get() == "abdominal swelling generalized":
        myLabel = Label(root, text="say with hepatomegaly, without hepatomegaly")
    elif e.get() == "with hepatomegaly":
        myLabel = Label(root, text="")
    # GERIATRICS
    # GYNECOLOGY
    # HEMATOLOGY
    # IMMUNOLOGY
    elif e.get() == "diagnosis cough":
        myLabel = Label(root, text="say diagnosis chills, fever, night sweats or say recent onset cough")
    elif e.get() == "diagnosis chills, fever, night sweats":
        myLabel = Label(root, text="diagnosis is an infections process, specify the kind of cough: recent onset cough, chronic or long standing cough, purulent sputum cough, hemoptysis cough, shortness of breath cough, weight loss cough")
    elif e.get() == "recent onset cough":
        myLabel = Label(root, text="consider bronchitis, pneumonia, congestive heart failure and pulmonary embolism")
    elif e.get() == "chronic or long standing cough":
        myLabel = Label(root, text="consider tuberculosis, bronchiectasis, congestive heart failure, asthma and chronic obstructive pulmonary disease")
    elif e.get() == "purulent sputum cough":
        myLabel = Label(root, text="consider pneumonia, tuberculosis and bronchiectasis")
    elif e.get() == "hemoptysis cough":
        myLabel = Label(root, text="consider tuberculosis, neoplasm, bronchiectasis, pulmonary embolism")
    elif e.get() == "shortness of breath cough":
        myLabel = Label(root, text="consider congestive heart failure, asthma, chronic obstructive pulmonary disease and pulmonary embolism")
    elif e.get() == "weight loss cough":
        myLabel = Label(root, text="consider neoplasm and tuberculosis")
    elif e.get() == "diagnosis consolidatio, crepitant rale, effusion":
        myLabel = Label(root, text="consider pneumonia, tuberculosis, congestive heart failure, pulmonary embolism")
    elif e.get() == "diagnosis sibilant and sonorous rale":
        myLabel = Label(root, text="consider asthma, bronchitis, chronic obstructive pulmonary disease")
    elif e.get() == "diagnosis hyperresonance":
        myLabel = Label(root, text="consider asthma, bronchitis, chronic obstructive pulmonary disease")
    elif e.get() == "diagnosis edema of one extremity, positive Homan's sign":
        myLabel = Label(root, text="diagnosis is pulmonary embolism")
    elif e.get() == "diagnosis edema of both extremities, cardiomegaly, hypertension, hepatomegaly, jugular venous distension":
        myLabel = Label(root, text="consider congestive heart failure")
    elif e.get() == "diagnosis decreased oxygen saturation":
        myLabel = Label(root, text="consider congestive heart failure, chronic obstructive pulmonary disease and pulmonary embolism")
    # NEPHROLOGY
    # NEUROLOGY
    elif e.get() == "diagnosis dizziness":
        myLabel = Label(root, text="differentiate true vertigo of dizziness (or light-headedness): if you have a sensation of your rotation or of your surroundings or if feel moving laterally, called lateral pulsion, then you have a true vertigo; otherwise you have dizziness. Now, say diagnosis true vertigo and diagnosis false vertigo")
    if e.get() == "diagnosis vertigo":
        myLabel = Label(root, text="differentiate true vertigo of dizziness (or light-headedness): if you have a sensation of your rotation or of your surroundings or if feel moving laterally, called lateral pulsion, then you have a true vertigo; otherwise you have dizziness. Now, say diagnosis true vertigo and diagnosis false vertigo")
    if e.get() == "diagnosis true vertigo":
        myLabel = Label(root, text="say: acute or recent vertigo, chronic recurrent vertigo, vertigo with tinnitus and hearing loss; vertigo with neurologic signs of ataxia, weakness, numbness, tingling of the extremities or face; do the tests ear, nose and throat examination; do a tests whisper; say gross neurologic examination vertigo; do: Hallpike maneuvers")
    if e.get() == "diagnosis false vertigo":
        myLabel = Label(root, text="say: vertigo diabetes; consider hypertension, any drugs the pacient may be on and anemia due to blood loss, say: chronic obstructive pulmonary disease or chronic anxiety; cervical bruit vertigo, hypertension vertigo, hypotension vertigo, slow pulse vertigo, heart mumur vertigo, rapid irregular heart rate vertigo, positive Chvostek's or Trosseau's sign vertigo")
    if e.get() == "acute or recent vertigo":
        myLabel = Label(root, text="consider acute labyrinthitis, impacted cerumen, foreign body, otitis media, vestibular neuronitis etc")
    if e.get() == "chronic recurrent vertigo":
        myLabel = Label(root, text="consider benign positional vertigo, Meniere's disease, cholesteatoma, acoustic neuroma, multiple sclerosis, vertebral-basilarinsufficiency and migraine")
    if e.get() == "vertigo with tinnitus and hearing loss":
        myLabel = Label(root, text="consider otitis media, Meniere's disease, cholesteatoma and acoustic neuroma")
    if e.get() == "vertigo with neurologic signs of ataxia, weakness, numbness, tingling of the extremities or face":
        myLabel = Label(root, text="consider acoustic neuroma, vertebral-basilar artery insufficiency and multiple sclerosis")
    if e.get() == "gross neurologic examination vertigo":
        myLabel = Label(root, text="if your gross neurologic examination is normal, therefore exclude multiple sclerosis, vertebral-basilar artery insufficiency and other space-occupying lesions")
    if e.get() == "vertigo diabetes":
        myLabel = Label(root, text="diagnosis is hypoglycemia from insulin or drugs")
    if e.get() == "chronic obstructive pulmonary disease or chronic anxiety":
        myLabel = Label(root, text="diagnosis is hyperventilation syndrome")
    if e.get() == "cervical bruit vertigo":
        myLabel = Label(root, text="diagnosis is carotid stenosis")
    if e.get() == "hypertension vertigo":
        myLabel = Label(root, text="if there is a difference in the blood pressure in each upper extremity, so diagnosis is subclavian steal")
    if e.get() == "hypotension vertigo":
        myLabel = Label(root, text="if there is a drop in blood pressure on standing, thus diagnosis is postural hypotension")
    if e.get() == "slow pulse vertigo":
        myLabel = Label(root, text="consider sick sinus syndrome and heart block")
    if e.get() == "heart mumur vertigo":
        myLabel = Label(root, text="consider aortic stenosis etc")
    if e.get() == "rapid irregular heart rate vertigo":
        myLabel = Label(root, text="diagnosis is auricular fibrillation")
    if e.get() == "positive Chvostek's or Trosseau's sign vertigo":
        myLabel = Label(root, text="diagnosis is hypocalcemia")
    if e.get() == "diagnosis headache":
        myLabel = Label(root, text="say intermittent headache, constant headache, acute headache, trauma headache, unilateral headache, bilateral headache, occipital and suboccipital headache, headache with fever, photophobia, noise sensitivity or nausea and vomiting headache, high blood pressure headache, visual disturbances headache, numbness, tingling or weakness of one or more extremities, ataxia, hearing loss, visual loss, facial paralysis, etc headache; visual acuity headache, papilledema headache, nuchal rigidity headache, focal changes in power, reflexes or sensation on the neurologic examination; if the headache is relieved by superficial temporal artery compression, thus it is most likely migraine or some other type of vascular headache; but if one of the temporal arteries is tender or enlarged, so it is temporal arteritis; say tests acute sinusitis; tenderness headache spray headache; measure the blood pressure in the body and in the both upper extremities, to rule out hypertensive headaches")
    if e.get() == "intermittent headache":
        myLabel = Label(root, text="consider migraine and cluster headache")
    if e.get() == "constant headache":
        myLabel = Label(root, text="consider sinusitis, meningitis, subarachnoid hemorrhage and tension headache")
    if e.get() == "acute headache":
        myLabel = Label(root, text="consider meningitis, subarachnoid hemorrhage, migraine, cluster headache and acute bacterial sinusitis")
    if e.get() == "trauma headache":
        myLabel = Label(root, text="consider subdural or epidural hematoma and postconcussion syndrome")
    if e.get() == "unilateral headache":
        myLabel = Label(root, text="consider migraine, cluster headache and temporal arteritis")
    if e.get() == "bilateral headache":
        myLabel = Label(root, text="consider common migraine and postconcussion syndrome")
    if e.get() == "occipital and suboccipital headache":
        myLabel = Label(root, text="consider tension headache, meningitis, subarachnoid hemorrhage, cervical spondylosis, hypertensive headaches and occipital neuralgia")
    if e.get() == "headache with fever":
        myLabel = Label(root, text="consider meningitis, sinusitis and infectious disease")
    if e.get() == "photophobia, noise sensitivity or nausea and vomiting headache":
        myLabel = Label(root, text="consider migraine, infectious disease, subarachnoid hemorrhage and space-occupying lesion")
    if e.get() == "high blood pressure headache":
        myLabel = Label(root, text="consider hypertensive headache and subarachnoid hemorrhage")
    if e.get() == "visual disturbances headache":
        myLabel = Label(root, text="consider migraine, refractive errors, astigmatism, space-occupying lesion")
    if e.get() == "numbness, tingling or weakness of one or more extremities, ataxia, hearing loss, visual loss, facial paralysis, etc headache":
    if e.get() == "visual acuity headache":
        myLabel = Label(root, text="try it to confirm glaucoma and refractive error")
    if e.get() == "papilledema headache":
        myLabel = Label(root, text="diagnosis is space-occupying lesion")
    if e.get() == "nuchal rigidity headache":
        myLabel = Label(root, text="subarachnoid hemorrhage and viral meningitis")
    if e.get() == "focal changes in power, reflexes or sensation on the neurologic examination":
        myLabel = Label(root, text="diagnosis is space-occupying lesions")
    if e.get() == "tenderness headache":
        myLabel = Label(root, text="if there is tenderness of an occipital nerve root, thus consider occipital neuralgia and confirm it with an occipital nerve block (there will be watering of one eye and possibly a running nose in acute cluster headache, but this will also be present in acute maxillary sinusitis; say limited range of motion headache)")
    if e.get() == "limited range of motion headache":
        myLabel = Label(root, text="limited range of motion of the cervical spine in the absence of nuchal rigidity means a diagnosis of cervical spondylosis (osteoarthritis)")
    if e.get() == "spray headache":
        myLabel = Label(root, text="if the spray Neo-Synephrine relieves the headache, therefore the diagnosis is allergic rhinitis or sinusitis")
    # OBSTETRICS
    # OPHTHALMOLOGY
    # ORTHOPEDY
    if e.get() == "diagnosis joint pain":
        myLabel = Label(root, text="if the pacient is over 50, he may have osteoarthritis; 30 to 40, rheumatoid arthritis etc; say recent trauma joint, repetitive use of the joint, fever or chills joint pain, single joint aching, multiple joints aching, rash joint pain, red eye joint pain, diabetes mellitus joint pain, family history of gout joint pain, urethral discharge joint pain, red and hot joint, swollen and tender joint; other forms of arthritis will have limited ROM on both active and passive movement, but bursitis and tendonitis will usually have limited ROM on active movement only; say subcutaneous nodules joint pain, heart murmurs or cardiomegaly joint pain. If the knee is aching, so check for loose collateral ligaments; do the McMurray’s test to verify torn meniscus, do the tests Lachman’s maneuver and say drawer sign joint pain. If the hip is aching, so palpate for a tender greater trochanter bursa to detect greater trochanter bursitis and if the positive Patrick’s test gives a positive result, then consider bursitis and arthritis, to confirm bursitis or/and tendonitis, inject the area with 1% to 2% lidocaine with or without 20 to 40 mg of triamcinolone acetonide, if you get total or nearly total relief and ROM is restored, then bursitis or tendonitis is almost certain")
    if e.get() == "recent trauma joint":
        myLabel = Label(root, text="consider sprain, fracture and dislocation")
    if e.get() == "loss of sensation in the thoracic dermatomes, motor change, reflex change, sensory change":
        myLabel = Label(root, text="consider thoracic spondylosis, herniated thoracic disk and space-occupying lesion of the thoracic spine")
    if e.get() == "repetitive use of the joint":
        myLabel = Label(root, text="consider bursitis, tendonitis and traumatic arthritis")
    if e.get() == "fever or chills joint pain":
        myLabel = Label(root, text="consider septic arthritis and rheumatic fever")
    if e.get() == "single joint aching":
        myLabel = Label(root, text="consider septic arthritis, osteoarthritis, gout, pseudogout and trauma")
    if e.get() == "multiple joints aching":
        myLabel = Label(root, text="consider rheumatoid arthritis, psoriatic arthritis, rheumatic fever, systemic lupus erythematosus [SLE], gonococcal arthritis etc")
    if e.get() == "rash joint pain":
        myLabel = Label(root, text="consider rheumatic fever, SLE, gonococcal arthritis and psoriasis")
    if e.get() == "red eye joint pain":
        myLabel = Label(root, text="consider conjunctivitis or iritis, both from Reiter’s syndrome or scleritis from rheumatoid arthritis")
    if e.get() == "diabetes mellitus joint pain":
        myLabel = Label(root, text="consider pseudogout and osteoarthritis")
    if e.get() == "family history of gout joint pain":
        myLabel = Label(root, text="diagnosis is gout")
    if e.get() == "urethral discharge joint pain":
        myLabel = Label(root, text="consider gonococcal arthritis and Reiter’s syndrome")
    elif e.get() == "red and hot joint":
        myLabel = Label(root, text="consider setic arthritis, gout, rheumatic fever and early rheumatoid arthritis")
    elif e.get() == "swollen and tender joint":
        myLabel = Label(root, text="diagnosis is osteoarthritis")
    elif e.get() == "subcutaneous nodules joint pain":
        myLabel = Label(root, text="consider rheumatoid arthritis and rheumatic fever")
    elif e.get() == "heart murmurs or cardiomegaly joint pain":
        myLabel = Label(root, text="consider rheumatic fever and systemic lupus erythematosus")
    elif e.get() == "drawer sign joint pain":
        myLabel = Label(root, text="diagnosis is anterior cruciate ligament tear")
    elif e.get() == "diagnosis low back pain":
        myLabel = Label(root, text="say trauma back pain, early age back pain, olderly age back pain, female back pain, male back pain; numbness, tingling or weakness in one or both lower extremities back pain; neurogenic claudication back pain, fever back pain, difficulty voiding back pain, erector spinae tenderness and spasm back pain, tender sacroiliac joints back pain; a positive straight leg raising test or femoral stretch test indicates herniated disk and other causes of radiculopathy; say dermatomal sensory loss, weakness, atrophy or reflex changes in one or both lower extremities back pain; tender boggy prostate back pain, unilateral short leg back pain, enlarged abdominal aorta with or without a bruit back pain, tender enlarged adnexa back pain, pelvic mass back pain; evaluate for malingering and hysteria, do this meanly if the back pain is produced or aggravated when both the hips and the spine are rotated simultaneously and when there is a negative straigh leg raise test facing a a positive straigh leg raise test while recumbent suggests malingering")
    elif e.get() == "back pain":
        myLabel = Label(root, text="consider sprain, fracture and herniated disk")
    elif e.get() == "early age back pain":
        myLabel = Label(root, text="consider rheumatoid spondylitis and spondylolisthesis")
    elif e.get() == "olderly age back pain":
        myLabel = Label(root, text="consider lumbar spondylosis and aortic aneurysm")
    elif e.get() == "female back pain":
        myLabel = Label(root, text="consider pelvic tumor, pelvic inflammatory disease and endometriosis")
    elif e.get() == "male back pain":
        myLabel = Label(root, text="consider prostatitis and prostatic carcinoma, with metastasis")
    elif e.get() == "numbness, tingling or weakness in one or both lower extremities back pain":
        myLabel = Label(root, text="consider herniated disk, spondylolisthesis, space-spaceoccupying lesion of the cauda equina and spinal stenosis")
    elif e.get() == "neurogenic claudication back pain":
        myLabel = Label(root, text="diagnosis is spinal stenosis")
    elif e.get() == "fever back pain":
        myLabel = Label(root, text="consider pelvic inflammatory disease and prostatitis epidural abscess")
    elif e.get() == "difficulty voiding back pain":
        myLabel = Label(root, text="consider prostatism and cauda equina syndrome")
    elif e.get() == "erector spinae tenderness and spasm back pain":
        myLabel = Label(root, text="consider lumbosacral sprain, fracture, herniated disk and lumbar spondylosis")
    elif e.get() == "tender sacroiliac joints back pai":
        myLabel = Label(root, text="diagnosis is rheumatoid spondylitis")
    elif e.get() == "dermatomal sensory loss, weakness, atrophy or reflex changes in one or both lower extremities back pain":
        myLabel = Label(root, text="consider herniated disk, other space-occupying lesions and spondylolisthesis")
    elif e.get() == "tender boggy prostate back pain":
        myLabel = Label(root, text="diagnosis is acute prostatitis")
    elif e.get() == "unilateral short leg back pain":
        myLabel = Label(root, text="diagnosis is scoliosis")
    elif e.get() == "enlarged abdominal aorta with or without a bruit back pain":
        myLabel = Label(root, text="diagnosis is aortic aneurysm")
    elif e.get() == "tender enlarged adnexa back pain":
        myLabel = Label(root, text="consider pelvic inflammatory disease and endometriosis")
    elif e.get() == "pelvic mass back pain":
        myLabel = Label(root, text="consider ovarian cyst or neoplasm, uterine fibroids or neoplasm etc")
    elif e.get() == "diagnosis painful shoulder":
        myLabel = Label(root, text="say: history of trauma painful shoulder, fever painful shoulder, do a tests cholecystitis; say pain radiating to the forearm, hand and fingers, weakness or numbness and tingling painful shoulder; palpate the subacromial bursa for tenderness, then have the pacient raise his shoulder until he experiences pain, let him drops the arm into your hands, if the pain disappears, thus diagnosis is subacromial bursitis from a torn rotator cuff, confirm this by testing passive range of motion of extension and abduction, if passive range of motion is full or almost, therefore subacromial bursitis is likely, but if both active and passive range of motion are impaired, so consider arthritis (gout, rheumatoid arthritis, osteoarthritis etc); furthermore, flex the biceps, if it causes pain in the anterior shoulder, thus diagnosis is biceps tendonitis, confirm it by palpating the biceps tendon at its origin in the shoulder; restriction of range of motion and both active and passive motion means frozen shoulder; mild diffuse atrophy of the upper extremities along with trophic changes in the skin means sympathetic dystrophy; tenderness in the joint means acromioclavicular pathology; many of these conditions can be further verified by relief of pain  with an injection of 3 to 5 mililiter of 1% to 2% lidocaine into the appropriate bursa, tendon or/and joint")
    elif e.get() == "history of trauma painful shoulder":
        myLabel = Label(root, text="consider sprain, fracture and dislocation")
    elif e.get() == "fever painful shoulder":
        myLabel = Label(root, text="consider osteomyelitis and subdiaphragmatic abcess")
    elif e.get() == "pain radiating to the forearm, hand and fingers, weakness or numbness and tingling painful shoulde":
        myLabel = Label(root, text="consider cervical radiculopathy from a herniated disk, cervical spondylosis, space-occupying lesion and thoracic outlet syndrome")
    # OTORHINOLARYNGOLOGY
    # PEDIATRICS
    # PSYCHIATRY
    # PULMONOLOGY
    elif e.get() == "diagnosis sore throat":
        myLabel = Label(root, text="say: fever and chills sore throat, rash sore throat, history of drug use sore throat, running nose sore throat, tremor and palpitations sore throat, pharyngeal exudates sore throat, strawberry tongue sore throat, Koplik spots, rash and conjuntivitis sore throat, posterior cervical adenopathy and rash sore throat, enlarged tender thyroid sore throat, enlarged spleen sore throat")
    elif e.get() == "fever and chills sore throat":
        myLabel = Label(root, text="consider various infectious conditions")
    elif e.get() == "rash sore throat":
        myLabel = Label(root, text="consider measles, nfectious mononucleosis etc")
    elif e.get() == "history of drug use sore throat":
        myLabel = Label(root, text="diagnosis is agranulocytosis")
    elif e.get() == "running nose sore throat":
        myLabel = Label(root, text="consider viral upper respiratory infection and measles")
    elif e.get() == "tremor and palpitations sore throat":
        myLabel = Label(root, text="diagnosis is subacute thyroiditis")
    elif e.get() == "pharyngeal exudates sore throat":
        myLabel = Label(root, text="consider strep pharyngitis, infectious mononucleosis, agranulocytosis, diphtheria etc")
    elif e.get() == "strawberry tongue sore throat":
        myLabel = Label(root, text="diagnosis is strep pharyngitis")
    elif e.get() == "Koplik spots, rash and conjuntivitis sore throat":
        myLabel = Label(root, text="diagnosis is measles")
    elif e.get() == "posterior cervical adenopathy and rash sore throat":
        myLabel = Label(root, text="diagnosis is infectious mononucleosis")
    elif i == "enlarged tender thyroid sore throat":
        print("diagnosis is subacute thyroiditis")
    elif i == "enlarged spleen sore throat":
        print("consider leukemia and infectious mononucleosis")
    # RADIOLOGY
    # RHEUMATOLOGY
    else:
        print('Done')
    y = y + 1
time.sleep(300)
