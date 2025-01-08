import pickle
from flask import Flask,request,abort
import requests
from app.Config import *
import json
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from pythainlp.tokenize import word_tokenize
from tensorflow.keras.models import load_model
import numpy as np


app=Flask(__name__)

@app.route('/webhook',methods=['POST','GET'])

def webhook():
    if request.method=='POST':
        payload = request.get_json()
        events = payload['events']
        model = load_model('BI_LSTM.h5')  
        with open('Tokenizer_Model.pickle', 'rb') as handle:
            tokenizer = pickle.load(handle)
        for event in events:
            event_type = event['type']
            if event_type == 'message':
                user_message = event['message']['text']
                tokenizer.fit_on_texts(user_message)
                text_to_predict = [user_message]
                tokenized_text = [word_tokenize(text, keep_whitespace=False) for text in text_to_predict]
                text_sequences = tokenizer.texts_to_sequences(tokenized_text)
                padded_sequence = pad_sequences(text_sequences, maxlen=7, padding="post")
                predicted_class = model.predict(padded_sequence)
                predicted_class_index = np.argmax(predicted_class)
                class_labels = [0, 1, 2, 3, 4, 5]
                predicted_label = class_labels[predicted_class_index]
                if predicted_label == 0 :
                    Reply_text = 'สวัสดีครับ ยินดีที่ได้รู้จักนะครับ ผมชื่อ "น้องฤกษ์เล่า" เป็นบอทช่วยให้คำแนะนำเกี่ยวกับการเลิกสุราและยาเสพติด\nน้องฤกษ์เล่าอยากให้พี่ๆ มีสุขภาพกายและสุขภาพจิตที่ดี เพื่อตนเองและคนที่เรารักครับ'
                elif predicted_label == 1 :
                    Reply_text = "น้องฤกษ์เล่า ขอแนะนำขั้นตอนเตรียมตัวในการเลิกดื่มสุรา ดังนี้:\n1.ตั้งเป้าหมายไว้ยึด เช่น เลิกเหล้าเพื่อสุขภาพ\n2.ฝึกปฏิเสธเมื่อถูกชักชวน เช่น ขอโทษนะเป็นโรคกระเพาะดื่มไม่ได้\n\n3.หากิจกรรมที่ชอบเพื่อทดแทน เช่น ดูหนัง ฟังเพลง\n4.หลีกเลี่ยงสิ่งกระตุ้นให้อยากดื่ม เช่น ร้านเหล้า วงเหล้า\n5.แก้อาการอยากดื่ม เช่น รีบทานอาหารให้อิ่ม จิบน้ำหวานบ่อยๆ\n6.ขอกำลังใจจากคนที่เรารัก และรักเรา\n7.เริ่มลด หรือ เลิกทันที... อย่ารอเดี๋ยว\n8.ลด หรือ เลิกดื่มวันต่อวัน และจงหมั่นชื่นชมตนเอง\n9. กำหนด และจำกัดปริมาณที่จะดื่ม แล้วให้ดื่มช้าๆ เพื่อจะได้มีสติในการยั้งคิด\n10. ทานอาหารก่อนดื่ม หรือดื่มพร้อมอาหาร ทำให้การดูดซึมของแอลกอฮอล์ช้าลง\n11. หลีกเลี่ยงอาหารรสเค็ม เพราะจะทำให้กระหายน้ำ จนต้องดื่มบ่อยขึ้น\n12.เลือกเครื่องดื่มที่มีความเข้มข้นของแอลกอฮอล์ต่ำ เช่น การดื่มเบียร์แทนสุราหรือไวน์ \n13. ดื่มแบบผสมให้เจือจาง เพื่อลดความเข้มข้นของแอลกอฮอล์\n14. ดื่มน้ำเปล่าสลับบ้างในระหว่างที่ดื่มสุรา เพื่อทิ้งช่วงในการดื่มให้ห่างขึ้น\n15. วางแผนกิจกรรมที่ให้ความสุขใจอย่างอื่นทดแทน เช่น กิจกรรมดนตรี เล่นกีฬา ทำงานศิลปะ งานอดิเรกต่างๆ \n16. หลีกเลี่ยงกลุ่มเพื่อนที่เคยดื่มด้วยกัน พบปะหรือเข้าร่วมกิจกรรมกับเพื่อนที่ไม่ดื่มแทน\n17. หากถูกชักชวนให้ดื่ม ปฏิเสธโดยตรงว่ามีปัญหาสุขภาพ หมอสั่งไม่ให้ดื่ม\n18. ไม่ควรขับขี่ยานพาหนะหลังดื่มสุรา\n19. งดการดื่ม เมื่อมีปัญหาสุขภาพเกิดขึ้น และไม่ควรดื่มสุราเมื่อมีการทานยาทุกชนิด\n\nโทร.1413 หรือ คลิก http://www.1413.in.th/ ศูนย์ปรึกษาปัญหาสุรา"
                elif predicted_label == 2 :
                    Reply_text = "น้องฤกษ์เล่า ขอแนะนำสิ่งที่ต้องทำความเข้าใจก่อนการพบแพทย์ ดังนี้:\n1. แผนกที่ช่วยเหลือเรื่องการบำบัดผู้ติดสุรา แผนกดังกล่าวก็คือแผนกจิตเวช หรือแผนกอื่นๆที่รับบำบัดรักษา เช่น\nเวชศาสตร์ตรอบครัว สินิกยาเสพติด หรือศูนย์ซับน้ำตา เป็นต้น\n2. สถานบำบัดที่ทำการบำบัดรักษาผู้ติดสุรา ผู้ติดสุราสามารถเข้ารับบริการได้ตามศูนย์บำบัดสุราและสารเสพติดตาม\nภูมิภาคต่างๆ สถานพยาบาลหรือโรงพยาบาลของรัฐที่มีแผนกจิตเวช หรือแผนกยาเสพติด ซึ่งโดยทั่วไปโรงพยาบาล\nประจำจังหวัดโดยส่วนใหญ่จะมีจิตแพทย์คอยให้ความช่วยเหลืออยู่\nสามารถหาตามลิงค์เหล่านี้ได้ดังนี้\n   2.1.https://web.facebook.com/notes/344596776832085/?_rdc=1&_rdr (โรงพยาบาลรัฐบาลในกรุงเทพฯและปริมณฑล)\n   2.2.https://web.facebook.com/notes/686174588675611/?_rdc=1&_rdr (โรงพยาบาลเอกชนในกรุงเทพฯและปริมณฑล)\n   2.3.https://web.facebook.com/notes/640345016661350/?_rdc=1&_rdr (โรงพยาบาลทั้งรัฐบาลและเอกชนในต่างจังหวัด)\n3. เอกสารที่ต้องเตรียมไป ได้แก่ บัตรประจำตัวประชาชน บัตรประจำตัวผู้ป่วย บัตรแสดงสิทธิการรักษา \n(เช่น บัตรทอง บัตรประกันสังคม เป็นต้น)\n4. สิทธิการรักษา ผู้ติดสุราสามารถขอใช้สิทธิกรรักษาเพื่อขอเบิกจ่าย หรือลดหย่อนด่รักษาพยาบาล ตามสิทธิการ\nรักษาที่ตนมีได้ เช่น บัตรทอง สิทธิประกันสังคม สวัสดิการข้ราชการ รัฐวิสาหกิจ เป็นต้น\n5.ขั้นตอนการพบแพทย์\n   5.1. เตรียมเอกสารที่ต้องใช้ติดต่อกับทางโรงพยาบาลให้ศรบถ้วน\n   5.2. ไปยังสถานพยาบาล หรือโรงพยาบาลที่มีการบำบัดรักษาเพื่อเลิกสุรา\n   5.3. ติดต่อทางเคาน์เตอร์ที่ทำบัตร หรือแผนกเวชระเบียนผู้ป่วยนอก ว่าต้องการมารับการบำบัดรักษาเพื่อเลิกสุรา\nโดยอาจน้นว่าต้องการรับการรักษา หรือขอคำปรึกษาจากจิตแพทย์\n   5.4. ทางโรงพยาบาลจะส่งไปที่แผนกจิตเวช หรือแผนกอื่นๆที่รับบำบัดรักษา\n   5.5. เมื่อพบแพทย์แล้วให้เล่รายละเอียดต่งๆของพฤติกรรมการดื่ม อาการต่างๆ ฯลฯ โดยให้ข้อมูลที่ถูกต้องแก่แพทยั\nเพื่อที่จะได้รับการวินิจฉัย และบำบัดรักษาที่เหมาะสมต่อไป\n   5.6. หากผู้ป่วยยังไม่ไปพบแพทย์ ญาติสามารถไปรับคำปรึกษาก่อนได้\n\nหาข้อมูลเพิ่มเติมได้ที่  http://www.1413.in.th/  ศูนย์ปรึกษาปัญหาสุรา"
                elif predicted_label == 3 :
                    Reply_text = "น้องฤกษ์เล่า ขอแนะนำผลกระทบของการดื่มสุรา มีดังนี้\n1.สมองและระบบประสาท\n    -ผลต่อสมอง มีอาการมึนเมา ง่วงนอน หลับ หมดสติ\n    -ระบบประสาทส่วนปลาย ทำให้มีอาการชาตามปลายมือ, ปลายเท้า\n    -ถ้าดื่มเครื่องดื่มแอลกอฮอล์เป็นประจำ หรือดื่มจนติดจะทำให้เกิดความจำเสื่อม ทำให้สมองเสื่อมเมื่อเอ็กซเรย์สมอง\n      จะพบว่าขนาดของสมองเล็กลง สูญเสียการทรงตัว เดินไม่ตรงทาง มีการเปลี่ยนแปลงทางบุคลิกภาพ ไม่สนใจสิ่งรอบข้าง \n      บางครั้งมีอาการเศร้าซึม หรือบางครั้งจะมีอาการประสาทหลอน ระแวงว่าจะมีคนมาทำร้าย\n2.ระบบทางเดินอาหารและตับ\n    -กระเพาะอาหาร ทำให้เกิดโรคกระเพาะอาหารอักเสบ เป็นแผลในกระเพาะ เลือดออกในกระเพาะอาหาร \n     เส้นเลือดดำที่หลอดอาหารโป่ง ก่อให้เกิดอาการปวดท้อง หรืออาเจียนเป็นเลือด\n    -ผลต่อตับอ่อน ทำให้ตับอ่อนอักเสบ มีอาการปวดท้องอย่างรุนแรง มีไข้ขึ้นสูง บางครั้งอาจทำให้เสียชีวิตได้\n    -ผลต่อตับ เมื่อดื่มนานเข้าจะทำให้เกิดโรคตับแข็ง ซึ่งจะมีอาการอ้วกเป็นเลือด ทำให้อาจเป็นมะเร็งตับได้ \n3.ระบบหัวใจและหลอดเลือด\n    -ระบบหัวใจ เมื่อดื่มแอลกอฮอล์มาก ๆ จะทำให้การเต้นและการบีบตัวของหัวใจไม่ปกติ หัวใจเต้นเร็วขึ้น \n     และขณะเดียวกันถ้าดื่มสุรามากจะขาดวิตามินบีหนึ่ง ก็จะทำให้กล้ามเนื้อของหัวใจทำงานไม่ปกติ\n    -ระบบหลอดเลือด แอลกอฮอล์จะทำให้เส้นเลือดขยายตัวและทำให้ไขมันในเลือดสูงทำให้เส้นเลือดแข็งตัวง่าย \n    ซึ่งจะทำให้เส้นเลือดในสมองแตกได้ง่าย ส่งผลให้เป็นอัมพาต อัมพฤกษ์ พิการชั่วชีวิตได้\n4.ระบบขับถ่ายและอวัยวะสืบพันธุ์\n    -เมื่อดื่มจนเรื้อรังจะทำให้ความต้องการทางเพศจะลดลง และส่งผลทำให้ลูกอัณฑะมีขนาดเล็กลงได้\n    -ในผู้หญิงตั้งครรภ์ จะทำให้เกิดการแท้งหรือคลอดบุตรเร็วกว่ากำหนด มีโอกาสทำให้เด็กที่กำลังจะเกิดมาเกิดมามีความผิดปกติได้สูง \n      ทำให้การสร้างเซลล์ประสาทและสมอง รวมถึงหัวใจ ตา แขน ขา อวัยวะ  \n      เพศของทารกผิดปกติ ทารกมีน้ำหนักตัวน้อย สมองเล็กกว่าปกติ เป็นโรคสมาธิสั้น รูปหน้าผิดปกติ ดวงตา กรามมีขนาดเล็ก ปลายจมูกพิการ\n5.ผลต่อวงจรการนอน\n    -แอลกอฮอล์จะช่วยให้หลับง่ายในช่วงแรกแต่เมื่อดื่มต่อเนื่องจะทำลายวงจรการนอนโดยตรง ทำให้ตื่นกลางคืน และมีปัญหาการนอนไม่หลับ\nหาข้อมูลเพิ่มเติมได้ที่ http://www.1413.in.th/  ศูนย์ปรึกษาปัญหาสุรา"
                elif predicted_label == 4 :
                    Reply_text = "ค้นหาสถานที่บำบัดใกล้บ้าน คลิก https://www.1413.in.th/Consults/treadment\nน้องฤกษ์เล่า ขอแนะนำกระบวนการบำบัดสุราตามความเหมาะสมของผู้ป่วย แต่มักมีขั้นตอนหลักๆ ดังนี้ :\n1.การปรึกษา (Counseling): การพูดคุยกับนักจิตวิทยาหรือผู้เชี่ยวชาญด้านการบำบัดเสพติดเพื่อให้คำปรึกษา\nและสนับสนุนในการแก้ไขปัญหาที่เกี่ยวข้องกับการดื่มสุราหรือการใช้สารเสพติด\n\n2.การรักษาทางยา (Medication-Assisted Treatment): บางครั้งจะใช้ยาเพื่อช่วยลดอาการของการเลิกใช้\nสารเสพติดหรือการลดความตายของการดื่มสุรา\n\n3.การฝึกทักษะในการดูแลตนเอง (Self-Care Skills Training): การฝึกทักษะในการจัดการกับความเครียด \nการดูแลสุขภาพที่ดี และทักษะการแก้ไขปัญหา\n\n4.การสนับสนุนจากชุมชน (Community Support): เข้าร่วมกลุ่มสนับสนุนที่มีคนที่มีปัญหาเดียวกัน \nหรือเข้าร่วมกิจกรรมที่สนับสนุนการหยุดดื่มสุรา\n\n5.การปฏิบัติธรรม (Mindfulness Practices): เช่น การทำสมาธิ หรือโยคะ เพื่อช่วยในการควบคุมอารมณ์\nและเพิ่มความตั้งใจในการหยุดดื่มสุรา\n\n6.การส่งเสริมสุขภาพ (Health Promotion): การเปลี่ยนแปลงพฤติกรรมที่เสี่ยงต่อการดื่มสุรา\nหรือการใช้สารเสพติด และการส่งเสริมสุขภาพที่ดี\n\n7.การรับคำปรึกษาจากครอบครัวและผู้ใกล้ชิด (Family and Social Support): ครอบครัวและผู้ใกล้ชิดมีบทบาทสำคัญ\nในการสนับสนุนและประคองผู้ที่มีปัญหาเหล่านี้\n\n8.การบำบัดสุราด้วยตัวเองหรือ self-detox หรือ self-rehabilitation ไม่แนะนำให้ทำเองโดยไม่มีคำปรึกษาหรือคำแนะนำ\nจากผู้เชี่ยวชาญทางการแพทย์หรือนักจิตวิทยาที่อาศัยอยู่ในหลักการของการแพทย์ที่มีประสบการณ์ในการจัดการปัญหา\nการใช้สุรา\n\nหาข้อมูลเพิ่มเติมได้ที่ http://www.1413.in.th/ ศูนย์ปรึกษาปัญหาสุรา"
                elif predicted_label == 5:
                    Reply_text = "น้องฤกษ์เล่า ขอแนะนำลิงค์สำหรับศึกษาอาการของการลงแดงด้วยการหักดิบและวิธีแก้อาการลงแดง ดังนี้:\n\nhttps://www.rama.mahidol.ac.th/ramamental/psychiatristknowledge/generalpsychiatrist/08062014-0911\n\nhttps://www.phufaresthome.com/blog/What-is-withdrawal-symptoms/"
                else :
                    Reply_text = "sad"
                print(Reply_text,flush=True)
                ReplyMessage(event['replyToken'],Reply_text,Channel_access_token)
        return request.get_json(),200
    elif request.method=='GET':
        return "this is method GET!!!",200
    else:
        abort(400)


def ReplyMessage(Reply_token,TextMessage,Line_Acees_Token):
    LINE_API='https://api.line.me/v2/bot/message/reply/'
    
    Authorization='Bearer {}'.format(Line_Acees_Token)
    print(Authorization)
    headers={
        'Content-Type':'application/json; char=UTF-8',
        'Authorization':Authorization
    }

    data={
        "replyToken":Reply_token,
        "messages":[{
            "type":"text",
            "text":TextMessage
        }
        ]
    }
    data=json.dumps(data) # ทำเป็น json
    r=requests.post(LINE_API,headers=headers,data=data)
    return 200