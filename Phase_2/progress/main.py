#import the necessary packages
from pickle import GET
from flask import Flask, render_template, request, session, redirect
import flask_excel as excel
import string
import random
import csv
import time

import os


letters = string.ascii_letters
eps_len_list = [15, 15, 15, 15, 15]
app = Flask(__name__)
# Setup the secret key and the environment
app.config.update(SECRET_KEY='osd(99092=36&462134kjKDhuIS_d23',
                  ENV='development')


@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        session["episode"] = 0 # initialize
        session['feedbacklist'] = [] # set up for appending feedback for each episode
        session['episodelength'] = 19 # 0 indexed
        session['episodemax'] = len(eps_len_list) - 1 # 0 indexed
        session["step"] = 1 # initialize
        return render_template('gdpr_age.html')

@app.route("/qualified", methods=["POST"])
def qualified():
    #active = np.genfromtxt("session_is_active.csv", delimiter=',')
    #if active == 1.0:
    #    return render_template("server_is_busy.html")
    qual = request.form.get('age18', False) and request.form.get('gdpr', False)
    if (qual):
        #sessionID = 'test string'
        session["sessionID"] = str(( ''.join(random.choice(letters) for i in range(10)) ))
        print("SessionID is ", session["sessionID"])
        return render_template("consent.html")
    else:
        return render_template("thanks.html")

@app.route("/consent", methods=["POST"])
def consent():
    user_info = {}
    user_info['agreed'] = request.form.get('agreed', False)
    sessionID = session["sessionID"]
    return render_template("info_training.html")

@app.route("/training", methods=["GET", "POST"])
def training():
    feedbacknum = None
    if request.method == "POST":
        score = request.form.get('score')
        if score is not None:
            feedbacknum = int(score)
            print(f"test feedback is {feedbacknum}")
    print("episode is ", session["episode"])
    if session['episode'] == 0:
        return render_template("info_training.html", feedback=feedbacknum)
    else:
        return render_template("stopped.html")

@app.route('/continuetofeedback', methods= ["POST"])
def continuetofeedback():
    info = request.form.get('info')
    print("Info in continuetofeedback", info)
    if info=="true":
        session['feedbacklist'] = []
        session['nextpage']="episode0step0.html"
        sessionID = session['sessionID']
        return redirect("/feedback", code=302)
    else:
        return render_template("excluded_participant.html")

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    thisvideo = "episode" + str(session["episode"]) + "step" + str(session["step"]) + ".mp4"
    if request.method == 'POST':
        proceed_to_next_episode = request.form.get('proceed_to_next_episode')
        if proceed_to_next_episode == 'true':
            return render_template("episodesteptemplate.html", sessionID=session["sessionID"], thisvideo=thisvideo, episode=session["episode"], step=session["step"])
        
        step = session["step"]
        feedbacknum = 999
        feedbacklist = session['feedbacklist']
        episode = session["episode"]
        session['episodelength'] = eps_len_list[episode]
        episodelength = session['episodelength']
        episodemax = session['episodemax']
        sessionID = session['sessionID']
        score = request.form.get('score')
        if score is not None:
            feedbacknum = int(score)
        if not feedbacknum == 999:
            if step < episodelength:
                step = step + 1
                session['step'] = step
                feedbacklist.append(feedbacknum)
                return render_template("episodesteptemplate.html", sessionID=session["sessionID"], thisvideo=thisvideo, episode=session["episode"], step=session["step"])
            elif episode < episodemax:
                feedbacklist.append(feedbacknum)
                module_dir = os.path.abspath(os.path.dirname(__file__))
                file_path = os.path.join(module_dir, "progress", "progress_" + str(sessionID) + ".csv")
                with open(file_path, 'a', newline='') as csvfile:
                    csvwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    csvwriter.writerow(feedbacklist)
                session["step"] = 1
                step = 1
                episode = episode + 1
                session['episode'] = episode
                session['feedbacklist'] = []
                return render_template("break.html")
            else:
                feedbacklist.append(feedbacknum)
                module_dir = os.path.abspath(os.path.dirname(__file__))
                file_path = os.path.join(module_dir, "progress", "progress_" + str(sessionID) + ".csv")
                with open(file_path, 'a', newline='') as csvfile:
                    csvwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    csvwriter.writerow(feedbacklist)
                return render_template("nasa_tlx.html", sessionID=session["sessionID"])
        else:
            return render_template("stopped.html")
    elif request.method == 'GET':
        return render_template("episodesteptemplate.html", sessionID=session["sessionID"], thisvideo=thisvideo, episode=session["episode"], step=session["step"])

def download_data(feedbacklist):
    #sample_data=[0, 1, 2]
    excel.init_excel(app)
    extension_type = "csv"
    filename = "test123" + "." + extension_type
    print(filename)
    d = {'colName': feedbacklist}
    print(d)
    return excel.make_response_from_dict(d, file_type=extension_type, file_name=filename)


from flask import request
import csv

@app.route('/submit_survey', methods=['POST'])
def submit_survey():
    # Retrieve data from form
    challenges = request.form.get('challenges')
    #robot_improvement = request.form.get('robot_improvement')
    teaching_effectiveness = request.form.get('teaching_effectiveness')
    alternative_preference = request.form.get('alternative_preference')
    confusion = request.form.get('confusion')
    effective_signal = request.form.get('effective_signal')

    # Use the session ID to match with the correct file
    sessionID = session.get('sessionID')
    if sessionID:
        module_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(module_dir, "progress", f"progress_{sessionID}.csv")

        with open(file_path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([challenges])
            #writer.writerow([robot_improvement])
            writer.writerow([teaching_effectiveness])
            writer.writerow([alternative_preference])
            writer.writerow([confusion])
            writer.writerow([effective_signal])
            csvfile.close()
            # writer.writerow([challenges,
            #                  robot_improvement,
            #                  teaching_effectiveness,
            #                  alternative_preference,
            #                  confusion,
            #                  effective_signal])
    
    # After writing, you can redirect the user to another page or show a success message
    return render_template("thankyou.html", sessionID=session.get("sessionID"))




@app.route('/thankyou', methods=['GET'])
def thankyou():
    # remove the username from the session if it is there
    session.pop('sessionID', None)
    session.pop("episode")
    session.pop('feedbacklist')
    session.pop('episodelength')
    session.pop('episodemax')
    session.pop("step")

if __name__ == '__main__':
    # defining server ip address and port
    app.run(host = '0.0.0.0', port= 15674)
