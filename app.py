from flask import Flask, render_template, request
import nltk
import nltk
nltk.download('wordnet')

from nltk import *
from nltk.corpus import *
global v
v=100

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/call_function', methods=['POST'])
def call_function():


    v = request.form.get('value')

    return 'Function called successfully'
@app.route('/', methods=['POST'])
def getvalue():
    print("aa" , v)
    if v==1:
        print('plagiarism')
    if v==2:
        print('paraphrase')
    if v==3:
        print('summarizer')
    text = request.form['text1']

    res = getsentence(text)
    print(res)
    return render_template("about.html", x=res)

# @app.route('/about')
# def about():
#     return render_template("about.html",x=text)

def get_synonyms(word):
    synonyms = set()
    for synset in wordnet.synsets(word):
        for lemma in synset.lemmas():
            synonyms.add(lemma.name())
    return synonyms


def calculate_similarity(synonym1, synonym2):
    synset1 = wordnet.synsets(synonym1)
    synset2 = wordnet.synsets(synonym2)

    if synset1 and synset2:  # Check if both synonyms have synsets
        similarity = synset1[0].wup_similarity(synset2[0])
        if similarity is not None:
            return similarity

    return 0  # If no similarity found or one of the synonyms has no synsets

def getsentence(s):
    stop_words = set(stopwords.words('english'))
    ps = ' '
    # words="Internet of Things (IoT) technology has transformed our lives, connecting various devices and enabling seamless communication. However, the rapid growth and widespread adoption of IoT have raised significant concerns about security. This abstract explores the challenges associated with IoT security and presents effective mitigation strategies. In this presentation, we will begin by providing an overview of IoT and its architecture, emphasizing the interconnected nature of devices, sensors, and networks. We will then delve into the unique security challenges that arise in IoT environments, such as device vulnerabilities, data privacy risks, and the potential for large-scale attacks. We will discuss the various attack vectors and threats that IoT systems face, including unauthorized access, data breaches, and denial-of-service (DoS) attacks. Through real-world examples, we will illustrate the potential consequences of these security breaches and their impact on individuals, businesses, and critical infrastructure. To address these challenges, we will present a range of mitigation strategies and best practices. These strategies will cover multiple layers of the IoT ecosystem, including device-level security, network infrastructure protection, and data management. We will explore authentication and access control mechanisms, secure communication protocols, encryption techniques, and anomaly detection systems. Furthermore, we will discuss the importance of collaboration between stakeholders, including manufacturers, service providers, and users, to establish a secure IoT ecosystem. We will emphasize the need for ongoing security assessments, regular software updates, and the incorporation of security measures throughout the entire lifecycle of IoT devices. Throughout the presentation, we will highlight the role of industry standards and regulations in ensuring IoT security. We will examine frameworks such as the NIST Cybersecurity Framework and the IoT Security Foundation's Best Practice Guidelines, providing attendees with guidance on compliance and industry-recognized security practices. By the end of this presentation, participants will have gained a comprehensive understanding of the security challenges inherent in IoT deployments and will be equipped with practical strategies to enhance the security of their own IoT systems. They will be empowered to implement effective mitigation measures, protecting sensitive data, preserving privacy, and ensuring the reliable and secure operation of IoT devices and networks."
    for i in s.split():
        if i in stop_words:
            ps += i + ' '
            continue
        synonym1 = i
        synonyms2 = get_synonyms(synonym1)
        if len(synonyms2) < 3:
            ps += i + ' '
            continue
        maximum = 0
        for j in synonyms2:
            if j != i:
                similarity_score = calculate_similarity(synonym1, j)
                if similarity_score > maximum:
                    sim_word = j
                    maximum = similarity_score
        ps += sim_word + ' '

        # print(f"Similarity between '{synonym1}' and '{j}': {similarity_score}")


    return ps


if __name__ == "__main__":
    app.run(debug=True)