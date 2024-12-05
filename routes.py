from flask import Flask,render_template,redirect,request,url_for,jsonify,Response
from sqlalchemy import delete
from models import Secret
import uuid
from cryptography.fernet import Fernet as f
import json

# key could be permanent
key = f.generate_key()
cipher = f(key)


def register_routes(app,db):
    @app.route('/')
    def index():
        return render_template('index.html')
    

    @app.route('/generate',methods=['GET','POST'])
    def generate():
    #getting data from form index.html
        secret_phrase = request.form.get('secret_phrase')
        secret_text = request.form.get('secret_text')

        #getting uuid secret key for comparing
        secret_key = str(uuid.uuid4())

        #hashing secret_phrase & secret_text
        hashed_phrase = cipher.encrypt(secret_phrase.encode('utf-8'))
        hashed_text = cipher.encrypt(secret_text.encode('utf-8'))

        secret = Secret(secret_phrase = hashed_phrase.decode('utf-8'),secret_text=hashed_text.decode('utf-8'),secret_key=secret_key)

        #adding in db
        db.session.add(secret)
        db.session.commit()

        if secret:
            return render_template('password.html',secret_key=secret_key,secret_phrase=hashed_phrase.decode())
        

    
        
    @app.route('/secret/<secret_key>',methods=['GET','POST'])
    def show(secret_key):
        secret = Secret.query.filter_by(secret_key=secret_key).first()
    

        if not secret:
            return render_template('error.html'),404
        
        #when getting data in enter_phrase.html
        if request.method == 'POST':
            #getting secret_phrase from form to compare with user's secret_phrase
            hashpas = request.form.get('secret_phrase')

            #decoding database's phrase
            db_phrase = cipher.decrypt(secret.secret_phrase.encode()).decode()
            
            #comparing
            if hashpas == db_phrase:
                decrypt_text = cipher.decrypt(secret.secret_text.encode()).decode()

                #only one-time secret! ! !
                db.session.delete(secret)
                db.session.commit()

                #getting json
                if request.args.get('format') == 'json':
                    db_text = cipher.decrypt(secret.secret_text.encode()).decode()
                    db_phrase = cipher.decrypt(secret.secret_phrase.encode()).decode()

                    db.session.delete(secret)
                    db.session.commit()

                    return jsonify({
                    'text': db_text,
                    'phrase': db_phrase
                    })
            
                
            return render_template('result.html',decrypt_text=decrypt_text)
        
        #when getting <secret_key> in URL -> request.method == get
        return render_template("enter_phrase.html")
        
            
        
        
            

        
                
            
        
    
    
    
    


    
    
        






















        
        #comparing with secret key inserted in URL
        # secret = Secret.query.filter_by(secret_key=secret_key).first()

        # if not secret:
        #     return 'secret not found',404
        
        # if request.method == 'POST':
        #     hashpas = request.form.get('secret_phrase')
        #     stored_phrase = cipher.decrypt(secret.secret_phrase.encode()).decode()

        #     if hashpas == stored_phrase:
        #         decryp_text = cipher.decrypt(secret.secret_text.encode()).decode()
        #         return render_template('result.html',decryp_text=decryp_text)
        #     else:
        #         return f'Ваш секрет не найден'
            
        # return render_template('enter_phrase.html')
        
