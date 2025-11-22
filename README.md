# Student GradeBook System

Ushbu loyiha talabalar profili, baholarni boshqarish, GPA avtomatik hisoblash va loglarni yuritish uchun mo‘ljallangan kichik modul hisoblanadi. Kod obyektga yo‘naltirilgan dasturlash (OOP) prinsiplariga asoslangan.


## Xususiyatlar

 Har bir talaba uchun yopiq (private) atributlar.
 Baholardan avtomatik GPA hisoblanadi.
 Qo‘shimcha metadata yozish imkoniyati.
 Log tizimi mavjud.
 Access control: admin/teacher/user huquqlariga ko‘ra cheklovlar.
 Talabalar ro‘yxati bilan ishlash.
 Demo funksiyasi orqali tizimni sinab ko‘rish mumkin.


## Loyiha tuzilishi
main.py
README.md

## Klasslar haqida

### StudentProfile
 Talabaning ismi va guruhi.
 Baholar ro‘yxati.
 Metadata saqlash.
 Avtomatik GPA hisoblash.
 Getter metodlar.

### GradeBook
 Talabalarni yaratish yoki mavjudini olish.
 Tanlangan talabaga baho qo‘shish.
 GPA avtomatik hisoblanadi.
 Loglarni saqlash va chiqarish.
 Hisobot chop etish.

### AccessControlledGradeBook
 “admin” yoki “teacher” bo‘lmasa, baho qo‘shish bloklanadi.
 GPA qo‘lda o‘zgartirilmaydi.


## Ishga tushirish
python main.py
Yoki kod ichidagi demo() funksiyasi avtomatik ishga tushadi.

## Demo haqida
Demo quyidagilarni bajaradi:
Ali va Laylo talabalarini yaratadi.
Ularning baholarini kiritadi.
GPA’ni hisoblaydi.
Hisobot chiqaradi.
Log yozuvlarini ko‘rsatadi.

## GPA hisoblash
Baholar 1–5 orasida bo‘ladi.
Formula:
Normalizatsiya:
(grade - 1) / 4
O‘rtacha qiymat olinadi.
4 ga ko‘paytiriladi.
round(..., 2) bilan yakuniy natija qaytariladi.

## Log tizimi
Tizimda har bir amal logga yoziladi:
Talaba yaratildi.
Baho qo‘shildi.
Ruxsat yo‘q bo‘lsa bloklandi.
GPA qo‘lda o‘zgartirilmasligi qayd etildi.
Log olish:
gb.get_logs()

## Kirish huquqlari
Access	Baho qo‘shish	GPA o‘zgartirish
admin	Ha	Yo‘q (avtomatik)
teacher	Ha	Yo‘q (avtomatik)
user	Yo‘q	Yo‘q
Kelajakda qo‘shilishi mumkin bo‘lgan imkoniyatlar

### JSON yoki database ga saqlash.
Guruh bo‘yicha o‘rtacha GPA hisoblash.
Talabani o‘chirish yoki yangilash.
Web API bilan integratsiya (FastAPI).
