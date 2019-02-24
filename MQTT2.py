import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import sys
 
#definicoes: 
Broker = "iot.eclipse.org"
PortaBroker = 1883
KeepAliveBroker = 60
TopicoSubscribe = "RenatoLobinho" #dica: troque o nome do topico por algo "unico", 
                                    #Dessa maneira, ninguem ira saber seu topico de
                                    #subscribe e interferir em seus testes
 
#Callback - conexao ao broker realizada
def on_connect(client, userdata, flags, rc):
    print("[STATUS] Conectado ao Broker. Resultado de conexao: "+str(rc))
    
    #faz subscribe automatico no topico
    client.subscribe(TopicoSubscribe)
 
#Callback - mensagem recebida do broker
def on_message(client, userdata, msg):
 MensagemRecebida = str(msg.payload)
    
 print("[MSG RECEBIDA] Topico: "+msg.topic+" / Mensagem: "+MensagemRecebida)
 if MensagemRecebida=="off-all": 
         client.publish(TopicoSubscribe,"off-coz")         
         client.publish(TopicoSubscribe,"off-qua")
         client.publish(TopicoSubscribe,"off-ban")
         client.publish(TopicoSubscribe,"off-gar")

 
 
 
#programa principal:
try:
        print("[STATUS] Inicializando MQTT...")
        #inicializa MQTT:
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        

        client.connect(Broker, PortaBroker, KeepAliveBroker)
       
        client.loop_forever()


except KeyboardInterrupt:
        print "\nCtrl+C pressionado, encerrando aplicacao e saindo..."
        sys.exit(0)
