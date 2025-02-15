 # // Khusus untuk link profil Facebook Lite atau m.fbeh

import requests
from bs4 import BeautifulSoup

class Finder:
    """
    Kelas Finder digunakan untuk menemukan ID pengguna dari tautan profil Facebook.
    """

    def __init__(self, link_profile: str):
        """
        Inisialisasi objek Finder dengan tautan profil Facebook.

        :param link_profile: Tautan profil Facebook yang akan dianalisis.
        """
        self.link_profile = link_profile

        # Header permintaan HTTP untuk mensimulasikan permintaan dari browser.
        headers = {
            'Host': 'facebook.com',
            'Port': '443',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36',
            'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        }

        # Mengirim permintaan GET ke tautan profil.
        session = requests.Session()
        response = session.get(self.link_profile, headers=headers)

        # Parsing konten HTML menggunakan BeautifulSoup.
        self.parser = BeautifulSoup(response.content, features="html.parser")

        # Mencari semua elemen <a> (tautan) pada halaman.
        self.content = self.parser.find_all('a')

    def get_user_id(self) -> str:
        """
        Mendapatkan ID pengguna dari tautan profil Facebook.

        :return: ID pengguna sebagai string.
        """
        try:
            # Mengambil elemen <a> tertentu yang berisi ID pengguna.
            target_link = self.content[2]['href']
            user_id = target_link.split('=')[4].replace('&refid', '')
            return user_id
        except (IndexError, KeyError, AttributeError):
            raise ValueError("Tidak dapat menemukan ID pengguna dari tautan profil.")

    def __repr__(self):
        """
        Representasi string dari objek Finder.

        :return: ID pengguna sebagai string.
        """
        return self.get_user_id()


if __name__ == "__main__":
    # Contoh penggunaan kelas Finder.
    try:
        # Ganti dengan tautan profil Facebook yang valid.
        link_profile = "https://m.facebook.com/profile.php?id=123456789"
        finder = Finder(link_profile)
        print(f"ID Pengguna: {finder}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
