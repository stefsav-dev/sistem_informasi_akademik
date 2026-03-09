# SPMB - Sistem Pendaftaran Mahasiswa Baru

Monorepo aplikasi **SPMB** yang terdiri dari:
- `backend` (FastAPI + SQLAlchemy + JWT Auth)
- `frontend` (Next.js + React + Tailwind + shadcn/ui)
- `mobile` (Flutter + Riverpod)

## Gambaran Singkat
Sistem ini menyediakan autentikasi berbasis role (`admin`, `dosen`, `mahasiswa`), manajemen profil pengguna, serta antarmuka web dan mobile untuk alur pendaftaran.

## Arsitektur Proyek
```text
spmb/
├── backend/   # REST API, autentikasi, role-based access, profil
├── frontend/  # Website (landing page, auth page, dashboard mahasiswa)
└── mobile/    # Aplikasi Flutter (introduction, login/register, home)
```

## Fitur Utama Saat Ini
- Registrasi akun dengan role.
- Login dengan `access token` dan `refresh token` JWT.
- Refresh token endpoint.
- Logout dengan token blacklist.
- Proteksi endpoint berbasis role.
- Manajemen profile user:
  - Buat profile
  - Lihat profile mahasiswa sendiri
  - Lihat profile mahasiswa by id (admin/dosen)
  - Lihat semua mahasiswa (admin/dosen)
  - Update profile
  - Hapus profile (admin)
- Frontend web untuk landing/auth/dashboard (UI masih tahap awal).
- Mobile app dengan onboarding + auth state dasar (tahap awal).

## Daftar Endpoint Backend
Base URL default: `http://localhost:8000`

- `GET /` - health/index
- `POST /register`
- `POST /login`
- `POST /refresh`
- `POST /logout`
- `GET /admin` (role: `admin`)
- `GET /dosen` (role: `dosen`, `admin`)
- `GET /mahasiswa` (role: `mahasiswa`)
- `POST /profile/create`
- `GET /profile/mahasiswa/me`
- `GET /profile/mahasiswa/{user_id}`
- `GET /profile/mahasiswa`
- `PUT /profile/update`
- `DELETE /profile/delete`

## Prasyarat
- Python 3.11+ (disarankan 3.12)
- Node.js 20+
- Flutter SDK 3.10+
- Database SQL sesuai `DATABASE_URL` (contoh PostgreSQL/MySQL/SQLite)

## Setup Backend
Masuk folder backend:

```bash
cd backend
```

Buat virtual environment dan install dependency:

```bash
python -m venv .venv
source .venv/bin/activate
pip install fastapi uvicorn sqlalchemy python-dotenv "python-jose[cryptography]" "passlib[bcrypt]" pydantic email-validator
```

Buat file `.env` di folder `backend`:

```env
DATABASE_URL=sqlite:///./spmb.db
SECRET_KEY=ganti_dengan_secret_anda
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=15
REFRESH_TOKEN_EXPIRE_DAYS=7
```

Jalankan server:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Dokumentasi API:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Setup Frontend (Web)
Masuk folder frontend:

```bash
cd frontend
npm install
npm run dev
```

Frontend berjalan di: `http://localhost:3000`

## Setup Mobile (Flutter)
Masuk folder mobile:

```bash
cd mobile
flutter pub get
flutter run
```

## Catatan Pengembangan
- `backend/Dockerfile` dan `frontend/Dockerfile` masih kosong (belum disiapkan).
- Frontend dan mobile masih berfokus pada struktur dan UI awal.
- Integrasi penuh frontend/mobile ke API backend masih dapat dilanjutkan.

## Status
Project berada pada tahap pengembangan aktif.
