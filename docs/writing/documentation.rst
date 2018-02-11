Dokumentasi
=============

.. image:: https://farm5.staticflickr.com/4279/35620636012_f66aa88f93_k_d.jpg

membaca adalah fokus utama bagi pengembang Python, di kedua proyek
dan kode dokumentasi . Ikutilah beberapa praktik terbaik sederhana yang dapat menghemat
waktu orang lain dan waktu anda.

Proyek Dokumentasi
---------------------

A :file:`README` file pada direktori root harus memberikan informasi umum bagi
pengguna maupun pengelola proyek. itu harus menjadi teks mentah atau
di dalam beberapa tulisan  sangat mudah untuk membaca markup, seperti :ref:`reStructuredText-ref`
atau Markdown. Ini harus berisi  dari  beberapa baris yang menjelaskan tujuan 
proyek atau perpustakaan (tanpa asumsi pengguna mengetahui tentang
proyek), URL sumber utama perangkat lunak, dan beberapa dasar kredit
informasi. File ini merupakan titik masuk utama untuk membaca kode.

An :file:`INSTALL` kurang dibutuhkan file dengan Python. Instalasi
instruksi sering dikurangi menjadi satu perintah, such as ``pip install
module`` or ``python setup.py install`` dan menambahkan :file:`README`
file.

A :file:`LISENSI` file harus *selalu* Hadir dan menetukan lisensinya
dimana perangkat lunak yang tersedia untuk umum.

A :file:`TODO` atau file ``TODO`` dalam bagian :file:`README` harus mendaftar itu
rencana untuk pengembangan kode.

A :file:`CHANGELOG` file atau bagian dalam :file:`README` harus menyusun pendek
gambaran dari perubahan dalam basis kode untuk versi terbaru.

Publikasi Proyek
-------------------

Tergantung pada proyek, dokumentasi Anda mungkin termasuk semua
atau beberapa komponen-komponen yang berikut:

- An *pengenalan* harus menunjukkan gambaran yang sangat singkat tentang apa yang
 dapat dilakukan dengan produk, Menggunakan satu atau menggunakan dua kasus yang sangat
 sederhana. Ini adalah puncak tiga puluh detik untuk proyek Anda.

- A *tutorial* harus menunjukkan beberapa pengguna utama secara lebih rinci. Pembaca
  akan mengikuti langkah demi langkah prosedur untuk set-up prototipe kerja.

- An *API referensi* biasanya dihasilkan dari kode (lihat
  :ref:`docstrings <docstring-ref>`). Ini akan mencantumkan semua antarmuka, parameter, dan nilai
  pengembalian yang tersedia untuk umum.

- *Dokumentasi pengembangan* ditujukan untuk kontributor potensial. Ini bisa
termasuk konvensi kode dan strategi desain umum proyek.

.. _sphinx-ref:

Sphinx
~~~~~~

Sphinx_ jauh dan jarak alat dokumentasi Python yang paling populer
. **Use it.**  ini mengubah :ref:`restructuredtext-ref` bahasa markup
ke berbagai format output termasuk HTML, LaTeX (for printable
PDF versions), halaman biasa, dan teks biasa.

Ada juga **great**, **free** hosting untuk anda Sphinx_ docs:
`Read The Docs`_. Gunakan. Anda bisa mengkonfigurasinya dengan commit untuk
repositori sumber Anda sehingga bisa membangun kembali dokumentasi Anda
terjadi secara otomatis.

ketika dijalankan, Sphinx_ akan mengimpor kode Anda dan menggunakan fitur introspeksi Python,
ia akan mengekstrak semua fungsi, metode dan tanda tangan kelas. Ini juga
akan mengekstrak docstrings yang menyertainya,  dan menyusun semuanya menjadi
dokumentasi yang terstruktur dan mudah dibaca untuk proyek Anda.  

.. Catatan::

    Sphinx terkenal dengan generasi API-nya, namun juga dengan berfungsi
    yang baik untuk dokumentasi proyek umum. panduan ini dibangun dengan
    Sphinx_ dan host ini d `Read The Docs`_

.. _Sphinx: http://sphinx.pocoo.org
.. _Read The Docs: http://readthedocs.org

.. _restructuredtext-ref:

reStructuredText
~~~~~~~~~~~~~~~~

Sebagian besar dokumentasi Python ditulis dengan reStructuredText_. Ini seperti 
penurunan dengan semua ekstensi opsional yang ada di dalamnya..

The `reStructuredText Primer`_ dan `reStructuredText Quick
Reference`_ should akan membantu Anda membiasakan diri dengan sintaks.

.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _reStructuredText Primer: http://sphinx.pocoo.org/rest.html
.. _reStructuredText Quick Reference: http://docutils.sourceforge.net/docs/user/rst/quickref.html


Saran dokumentasi kode
-------------------------

Komentar memperjelas kode dan ditambahkan dengan tujuan membuat
kode lebih mudah dipahami. dengan Python, comments komentar dimulai dengan hash
(tanda Nomor) (``#``).

.. _docstring-ref:

Dengan Python, *docstrings* menjelaskan modul, kelas, dan fungsinya:

.. code-block:: python

    def square_and_rooter(x):
        """Return the square root of self times self."""
        ...

secara umum, Ikuti bagian komentar :pep:`8#comments` (the "paduan gaya
phyton"). Informasi lebih lanjut tentang docstrings dapat ditemukan di :pep:`0257#specification` (The Docstring Conventions Guide).

Mengomentari Bagian Kode
~~~~~~~~~~~~~~~~~~~~~~~~~~~

*jangan gunakan triple-quote string untuk kode komentar*. ini bukan kelakuan yang
bagus, karena line-oriented command-line alat seperti grep akan
tidak menyadari bahwa kode berkomentar aktif. Lebih baik menambahkan hash
pada tingkat indentasi yang tepat untuk setiap baris komentar. anda
Editor mungkin memiliki kemampuan untuk melakukan ini dengan mudah
dan perlu mempelajari komentar / tanda komentar untuk beralih.

Doktrin and sihir
~~~~~~~~~~~~~~~~~~~~

beberapa alat menggunakan doktrin untuk menanamkan lebih-dari pada-dokumentasi perilaku,
Seperti jenis tes logika. Mereka dapat bagus, tapi kamu tidak akan pernah pergi
salah dengan vanilla "Berikut adalah apa yang dilakukan."

alat seperti Sphinx_ anda akan mengurai doktrin sebagai reStructuredText dan merendernya dengan
benar sebagai HTML. THal ini membuat sangat mudah untuk menanamkan potongan contoh kode
dalam dokumentasi proyek.

Selain itu, Doctest_ akan membaca semua doktrin  tertanam yang terlihat
seperti masukan dari commandline Python (diawali dengan ">>>") dan menjalankannya,  memeriksa apakah
output dari perintah sesuai dengan teks pada baris berikut. hal
ini memungkinkan pengembang untuk menanamkan contoh nyata dan penggunaan fungsi di samping
kode sumber mereka, dan sebagai efek, i ini juga memastikan kode mereka
diuji dan berfungsi.

::
    
    def my_function(a, b):
        """
        >>> my_function(2, 3)
        6
        >>> my_function('a', 3)
        'aaa'
        """
        return a * b

.. _Doctest: https://docs.python.org/3/library/doctest.html

Doktrin versus Blok Komentar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ini tidak bisa digantikan. Untuk fungsi atau ruang, blok komentar 
terdepan adalah catatan pemrogram. doktrin menjelaskan
*pengoperasian* fungsi atau ruang:

.. code-block:: python

    # This function slows down program execution for some reason.
    def square_and_rooter(x):
        """Returns the square root of self times self."""
	...

Tidak seperti blok komentar, doktrin dibangun ke dalam bahasa Python itu sendiri.
Ini berarti Anda dapat menggunakan semua kemampuan introspeksi kuat Python untuk
mengakses docstrings saat waktu berjalan, dibandingkan dengan komentar yang dioptimalkan.
Doktrin dapat diakses dari `__doc__` dunder atribut untuk hampir
setiap objek Python, dan juga dengan `help()` fungsi.

Sementara blok komentar biasanya digunakan untuk menjelaskan *apa* bagian kode yang di
lakukan, atau spesifik dari suatu algoritma, doktrin yang lebih ditujukan  
untuk menjelaskan kepada pengguna lain dari kode Anda (atau Anda dalam waktu 6 bulan) *bagimana*
fungsi tertentu dapat digunakan dan tujuan umum fungsi, kelas,
atau modul.

menulis doktrin
~~~~~~~~~~~~~~~~~~

Bergantung pada kompleksitas fungsi, metode, atau kelas yang sedang ditulis,
dokumentasi satu baris mungkin sangat sesuai. Ini umumnya digunakan untuk ,
kasus yang benar-benar jelas, seperti::

    def add(a, b):
        """Add two numbers and return the result."""
        return a + b

Doktrin harus menggambarkan fungsinya dengan cara yang mudah dimengerti.
Untuk kasus sederhana seperti fungsi sepele dan ruang, scukup embedding tanda 
tangan fungsi (i.e. `add(a, b) -> result`) di doktrin tidak diperlukan
Ini di karena dengan modul pemeriksaan Python,  sudah cukup mudah
untuk menemukan informasi ini jika diperlukan, dan ini juga tersedia 
dengan membaca sumber kodenya. 

Namun dalam proyek yang lebih besar atau lebih kompleks, Seringkali ide bagus untuk diberikan
Informasi lebih lanjut tentang fungsi, apa fungsinya, pengecualian apa pun yang mungkin diajukan, 
apa masalahnya, atau rincian yang relevan tentang parameter.

Untuk dokumentasi kode gaya populer yang lebih rinci digunakan untuk
Proyek Numpy, yang sering disebut dengan doktrin `Numpy style`_. Sementara itu bisa mengambil
lebih banyak garis dari contoh sebelumnya, memungkinkan pengembang untuk menyertakan lebih
banyak informasi tentang metode, fungsi, atau kelas. ::

    def random_number_generator(arg1, arg2):
        """
        Summary line.

        Extended description of function.

        Parameters
        ----------
        arg1 : int
            Description of arg1
        arg2 : str
            Description of arg2

        Returns
        -------
        int
            Description of return value

        """
        return 42

dengan `sphinx.ext.napoleon`_ Plugin memungkinkan Sphinx untuk mengurai gaya
doktrin, msehingga mudah untuk menggabungkan doktrin gaya NumPy ke dalam
proyek Anda

pada akhir hari, tidak masalah apa gaya yang digunakan untuk menulis
doktrin, ttujuan mereka adalah untuk melayani sebagai dokumentasi bagi siapa saja yang mungkin 
perlu membaca atau membuat perubahan pada kode Anda. selama itu benar, dimengerti
dan mendapat poin yang relevan, maka hal itu telah dilakukan pekerjaan yang dirancangnya.


Untuk bacaan lebih lanjut tentang doktrin, silakan berkonsultasi dengan :pep:`257`

.. _thomas-cokelaer.info: http://thomas-cokelaer.info/tutorials/sphinx/docstring_python.html
.. _sphinx.ext.napoleon: https://sphinxcontrib-napoleon.readthedocs.io/
.. _`NumPy style`: http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html

Alat lainnya
-----------

Anda mungkin melihat ini di alam bebas. Use :ref:`sphinx-ref`.

Pycco_
    Pycco adalah "Melek-program-gaya dokumentasi generator"
    dan merupakan port dari  node.js Docco_.  Ini membuat kode menjadi
    kode HTML dan dokumentasi sisi-demi-sisi.

.. _Pycco: https://pycco-docs.github.io/pycco/
.. _Docco: http://jashkenas.github.com/docco

Ronn_
    Ronn membangun manual Unix. Ini mengubah teks teks yang dapat dibaca 
    manusia menjadi layar utama, dan juga HTML untuk web.

.. _Ronn: https://github.com/rtomayko/ronn

Epydoc_
    Epydoc dihentikan. gunakan :ref:`sphinx-ref` sebagai gantinya.

.. _Epydoc: http://epydoc.sourceforge.net

MkDocs_
    MkDocs adalah generator situs statis yang cepat dan sederhana yang diarahkan
   untuk membuat dokumentasi proyek dengan Markdown.

.. _MkDocs: http://www.mkdocs.org/
