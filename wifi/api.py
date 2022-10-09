from time import sleep
import pywifi
from pywifi import const, Profile
from pywifi.iface import Interface


def interfaces() -> list[dict[str, Interface | int]]:
    """ 获取本机全部网卡，按照对象返回 {网卡名， 连接状态， 网口对象} """
    wifi = pywifi.PyWiFi()
    wifi_data = []
    for item in wifi.interfaces():
        wifi_data.append({
            'name': item.name(),
            'status': item.status(),
            'content': item
        })
    return wifi_data


def get_interface(index: int) -> Interface:
    """ 获取指定的网卡对象 """
    return interfaces()[index]['content']


def disconnect(interface: Interface) -> None:
    """ 断开所有 wifi 连接 """
    return interface.disconnect()


def scan_port(interface: Interface, scan_time: int = 4) -> list[dict[str, Profile]]:
    """ 扫描网卡当前网络的wifi """
    interface.scan()
    sleep(scan_time)
    interface_data = []
    for item in interface.scan_results():
        interface_data.append({
            'name': item.ssid.encode('raw_unicode_escape').decode('utf-8'),
            'content': item
        })
    return interface_data


def connect(wifi: Profile):
    """ 创建连接对象 """
    profile = pywifi.Profile()
    # 编辑连接对象
    profile.ssid = wifi.ssid
    profile.auth = wifi.auth
    profile.akm = wifi.akm
    profile.cipher = const.CIPHER_TYPE_CCMP
