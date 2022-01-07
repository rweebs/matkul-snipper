Cara gunainnya
<ol>
    <li>Setup virtual environtment </li>
    <ul>
        <li>
        Menggunakan poetry. Install poetry di<a href="https://python-poetry.org/docs/#installation">sini</a>
        <ol>
            <li>Download dependencies</li>
            > poetry install
            <li>Aktifkan shell (sama dengan virtual env)</li>
            > poetry shell
        </ol>
        </li>
        <li>
        Menggunakan pip biasa
        <ol>
            <li>Install virtualenv jika belum punya</li>
                > pip install virtualenv
            <li>Buat virtual env</li>
                > virtualenv venv
            <li>Aktifkan virtual env</li>
                <p>Untuk windows run `venv\Scripts\activate`</p>
                <p>Untuk linux run `source venv/bin/activate`</p>
            <li>Download dependencies</li>
                > pip install -r requirements.txt
        </ol>
        </li>
    </ul>
    <li>rename .env.example jadi .env </li>
    <li>isi data data nya</li>
    <li>Ambil cookie dan user agent dari inspect element di bagian network check yang statusmhs. SS: <image src='./ss.png' />
    </li>
    <li> Run main program</li>
        > python main.py
</ol>


Youtube Tutorial : https://www.youtube.com/watch?v=_14Z49FxUoA
