from scapy.all import sniff
from scapy.layers.dns import DNSQR
from sender import enviar_log
from cache import dominio_reciente
from filters import dominio_permitido


def procesar_paquete(packet):

    try:

        if packet.haslayer(DNSQR):

            dominio = packet[DNSQR].qname.decode().rstrip(".")

            if not dominio_permitido(dominio):
                return

            if dominio_reciente(dominio):
                return

            print("Dominio detectado:", dominio)

            enviar_log(dominio)

    except Exception as e:

        print("Error procesando paquete:", e)


def iniciar_monitoreo():

    print("Iniciando monitoreo DNS...")

    sniff(
        filter="udp port 53",
        prn=procesar_paquete,
        store=False
    )


if __name__ == "__main__":

    iniciar_monitoreo()