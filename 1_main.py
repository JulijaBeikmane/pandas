
from dati import dotie_jautajumi
from jautajuma_modelis import Jautajumi
from viktorinas_pamats import QuizBrain

jautajumu_banka = []
for jautajums in dotie_jautajumi:
    jaut_teksts = jautajums["jaut"]
    jaut_atbilde = jautajums["atbilde"]
    jauns_jaut = Jautajumi(jaut_teksts, jaut_atbilde)
    jautajumu_banka.append(jauns_jaut)

viktorina = QuizBrain(jautajumu_banka)
while viktorina.vel_ir_jautajumi():
    viktorina.nakamais_jaut()
