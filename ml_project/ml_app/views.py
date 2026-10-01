import os
from django.shortcuts import render
from django.http import HttpResponse
import joblib

# Resolve model paths relative to project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCALER_PATH = os.path.join(BASE_DIR, 'scalermodel.pkl')
MODEL_PATH = os.path.join(BASE_DIR, 'mlmodel.pkl')

_scaler = None
_model = None

def get_models():
    global _scaler, _model
    if _scaler is None:
        _scaler = joblib.load(SCALER_PATH)
    if _model is None:
        _model = joblib.load(MODEL_PATH)
    return _scaler, _model

GLASS_INFO = {
    1: {
        'id': 1,
        'title': 'Building Windows (Float Processed)',
        'category': 'Architectural Flat Glass',
        'badge': 'Float Processed',
        'icon': '🏢',
        'summary': 'Standard architectural plate glass manufactured by floating molten glass onto a molten tin bath. Produces exceptionally flat, uniform, and distortion-free sheets.',
        'uses': 'Commercial curtain walls, storefronts, double-glazed architectural windows, interior architectural glazing.',
        'properties': 'High optical clarity, uniform thickness, excellent planarity, receptive to low-E thermal coatings.',
        'silica_profile': 'Standard Soda-Lime (High Silica ~72%)'
    },
    2: {
        'id': 2,
        'title': 'Building Windows (Non-Float Processed)',
        'category': 'Architectural Sheet Glass',
        'badge': 'Drawn / Rolled',
        'icon': '🏛️',
        'summary': 'Architectural sheet or rolled glass made using traditional vertical drawing or rolling methods without a tin bath. Retains slight characteristic surface wave.',
        'uses': 'Heritage and historic building restoration, greenhouse glazing, patterned/frosted glass, interior partitions.',
        'properties': 'High surface hardness, traditional aesthetic, cost-effective structural sheet glass.',
        'silica_profile': 'Traditional Soda-Lime Sheet Formulation'
    },
    3: {
        'id': 3,
        'title': 'Vehicle Windows (Float Processed)',
        'category': 'Automotive Safety Glass',
        'badge': 'Automotive Float',
        'icon': '🚗',
        'summary': 'Precision automotive-grade soda-lime float glass engineered for strict optical distortion standards and compatibility with thermal tempering and PVB lamination.',
        'uses': 'Automotive windshields, laminated panoramic roofs, tempered side door windows, rear windshields.',
        'properties': 'High impact resistance when laminated/tempered, controlled light transmission, UV-absorbing formulation.',
        'silica_profile': 'Automotive Float with Controlled Iron'
    },
    4: {
        'id': 4,
        'title': 'Vehicle Windows (Non-Float Processed)',
        'category': 'Automotive Specialty Glass',
        'badge': 'Specialty Automotive',
        'icon': '🚚',
        'summary': 'Custom cast or pressed safety glass formulations manufactured for curved vehicular profiles, specialty industrial vehicles, or armored transports.',
        'uses': 'Heavy machinery operator cabs, specialized transport vehicles, historic automotive restorations, marine wheelhouses.',
        'properties': 'Heavy-duty structural resilience, vibration resistance, reinforced fracture profile.',
        'silica_profile': 'High-Impact Reinforced Matrix'
    },
    5: {
        'id': 5,
        'title': 'Containers & Packaging Ware',
        'category': 'Packaging & Container Glass',
        'badge': 'Container Ware',
        'icon': '🍾',
        'summary': 'Soda-lime-silica container glass formulated for rapid mechanical forming in Individual Section (IS) blow-mold machines with high chemical durability.',
        'uses': 'Pharmaceutical bottles, wine & beer containers, food preservation jars, chemical reagents bottles.',
        'properties': '100% recyclable, impermeable to gases and aromas, chemical inertness, high burst pressure.',
        'silica_profile': 'High-Alumina Rapid-Setting Container Formula'
    },
    6: {
        'id': 6,
        'title': 'Tableware & Household Glass',
        'category': 'Domestic Household Glass',
        'badge': 'Tableware & Domestic',
        'icon': '🍽️',
        'summary': 'Formulated with low magnesium and balanced alumina for enhanced brilliance, high scratch resistance, and resilience against aggressive dishwasher detergents.',
        'uses': 'Tumblers, wine glasses, glass cookware, dessert bowls, serving platters.',
        'properties': 'Exceptional brilliance, surface smoothness, scratch resistance, hygienic non-porous structure.',
        'silica_profile': 'Low-Magnesium High-Clarity Tableware'
    },
    7: {
        'id': 7,
        'title': 'Headlamps & Technical Optics',
        'category': 'Automotive / Technical Lighting',
        'badge': 'Thermal Technical Glass',
        'icon': '💡',
        'summary': 'Specialized borosilicate or barium-doped glass engineered with high thermal shock endurance to withstand sudden temperature shifts from bulb heat and rain spray.',
        'uses': 'Automotive headlight lenses, high-intensity fog lamps, projection optics, industrial floodlight covers.',
        'properties': 'Low thermal expansion coefficient, resistance to sudden thermal shock, high thermal gradient tolerance.',
        'silica_profile': 'High-Barium Thermal Resistance Matrix'
    }
}

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    try:
        scaler, mlmodel = get_models()
        keys = ['Ri', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe']
        defaults = [1.52101, 13.64, 4.49, 1.10, 71.78, 0.06, 8.75, 0.0, 0.0]
        
        values = []
        for i, key in enumerate(keys):
            val = request.GET.get(key)
            if val is not None and val.strip() != '':
                values.append(float(val))
            else:
                values.append(defaults[i])
        
        scaled_input = scaler.transform([values])
        ans = int(mlmodel.predict(scaled_input)[0])
        
        # Calculate chemical metrics (total oxide weight %)
        total_oxides = round(sum(values[1:]), 2)
        info = GLASS_INFO.get(ans, GLASS_INFO[1])
        
        context = {
            'ans': ans,
            'list': values,
            'info': info,
            'total_oxides': total_oxides,
            'all_types': GLASS_INFO
        }
        return render(request, 'result.html', context)
    except Exception as e:
        context = {
            'ans': 1,
            'list': [1.52101, 13.64, 4.49, 1.10, 71.78, 0.06, 8.75, 0.0, 0.0],
            'info': GLASS_INFO[1],
            'total_oxides': 99.82,
            'all_types': GLASS_INFO,
            'error': str(e)
        }
        return render(request, 'result.html', context)
        