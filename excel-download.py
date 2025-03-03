import pandas as pd
import random
from datetime import datetime, timedelta

# تعريف البيانات الأساسية
employees = [
    "أحمد محمد", "سارة علي", "محمود إبراهيم", "فاطمة أحمد", "عمر خالد",
    "نور حسن", "ياسر سمير", "ليلى كمال", "كريم عادل", "رنا سعيد"
]

suppliers = [
    "فارما للأدوية", "الدولية للصناعات الدوائية", "المصرية للأدوية",
    "العربية للمستحضرات", "النيل للأدوية", "الشرق للصناعات الدوائية",
    "المتحدة للأدوية", "الوطنية للمستحضرات", "الخليج للأدوية", "الأمل للصناعات الطبية",
    "الغد للصناعات الدوائية", "النهضة للأدوية", "السلامة للصناعات الطبية", "الرفاعي للأدوية",
    "الزهراء للأدوية", "الطبية المتقدمة", "الرائدة للصناعات", "الطبية الحديثة", "الطبية الدولية"
]

medications = [
    {"name": "باراسيتامول", "basePrice": 50},
    {"name": "أموكسيسيلين", "basePrice": 75},
    {"name": "أوميبرازول", "basePrice": 100},
    {"name": "ميتفورمين", "basePrice": 85},
    {"name": "سيتالوبرام", "basePrice": 120},
    {"name": "إيبوبروفين", "basePrice": 45},
    {"name": "ديكلوفيناك", "basePrice": 60},
    {"name": "سيتريزين", "basePrice": 40},
    {"name": "راميبريل", "basePrice": 95},
    {"name": "أتورفاستاتين", "basePrice": 150},
    {"name": "فيتامين سي", "basePrice": 30},
    {"name": "فيتامين د", "basePrice": 35},
    {"name": "أدوية البرد", "basePrice": 55},
    {"name": "أدوية الحساسية", "basePrice": 65},
    {"name": "أدوية الضغط", "basePrice": 90},
    {"name": "أدوية السكري", "basePrice": 110},
    {"name": "أدوية الكوليسترول", "basePrice": 130},
    {"name": "أدوية الصداع", "basePrice": 40},
    {"name": "أدوية المعدة", "basePrice": 70},
    {"name": "أدوية العظام", "basePrice": 80}
]

# دالة لتوليد تاريخ عشوائي
def generate_random_date():
    end = datetime.now()
    start = end - timedelta(days=365)
    random_date = start + timedelta(days=random.randint(0, 365))
    return random_date

# دالة لتوليد طلبية واحدة
def generate_order(index):
    # اختيار موظف عشوائي
    employee = random.choice(employees)
    
    # اختيار مورد عشوائي
    supplier = random.choice(suppliers)
    
    # اختيار دواء عشوائي
    medication = random.choice(medications)
    
    # توليد تاريخ طلب عشوائي
    order_date = generate_random_date()
    
    # جعل الكمية مختلفة بشكل واضح بين الموظفين والموردين
    quantity = random.randint(30, 300) * (employees.index(employee) + 1)  # تعتمد على الموظف
    
    # جعل الخصم مختلفًا بشكل واضح بين الموردين
    discount = random.uniform(0.2, 0.5) * (suppliers.index(supplier) + 1) / len(suppliers)  # تعتمد على المورد
    
    # جعل التقييم مختلفًا بشكل واضح بين الموظفين
    quality = random.randint(1, 10) + (employees.index(employee) % 2)  # تعتمد على الموظف
    
    # جعل مدة التوصيل مختلفة بشكل واضح بين الموردين
    delivery_days = random.randint(14, 200) + (suppliers.index(supplier) % 3)  # تعتمد على المورد

    # حساب السعر قبل وبعد الخصم
    price_before_discount = medication["basePrice"] * quantity
    price_after_discount = price_before_discount * (1 - discount)
    
    # حساب تاريخ التسليم
    delivery_date = order_date + timedelta(days=delivery_days)

    return {
        'رقم الطلبية': index + 1,
        'الموظف المسؤول': employee,
        'المورد': supplier,
        'اسم الدواء': medication["name"],
        'تاريخ الطلب': order_date.strftime('%Y-%m-%d'),
        'تاريخ التسليم': delivery_date.strftime('%Y-%m-%d'),
        'الكمية': quantity,
        'السعر قبل الخصم': round(price_before_discount, 2),
        'نسبة الخصم': f"{round(discount * 100, 2)}%",
        'السعر بعد الخصم': round(price_after_discount, 2),
        'تقييم الجودة': quality,
        'مدة التوصيل (أيام)': delivery_days
    }

# توليد البيانات
data = [generate_order(i) for i in range(5000)]

# إنشاء DataFrame
df = pd.DataFrame(data)

# حفظ البيانات في ملف Excel
df.to_excel("pharmacy_purchases_data_updated_v2.xlsx", index=False)
print("تم إنشاء الملف بنجاح!")