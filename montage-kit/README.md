<div dir="rtl">

# 🎬 Montage Kit — عدّة المونتاج الكاملة

كل ما يحتاجه المونتير في مجلد واحد: **42 حركة ومؤثر** · **56 انتقال** · **79 مؤثر صوتي** · **29 فلتر ألوان** · **20 طبقة ضوئية**، بالإضافة لستيكرات النيون من المجلد الرئيسي.

كل شيء هنا مصنوع بالكود من الصفر، **بدون أي حقوق ملكية**، فتقدر تستخدمه في يوتيوب وتيك توك وإنستغرام والإعلانات التجارية بحرية.

https://github.com/barhoom98/glowing-icons/raw/main/montage-kit/previews/demo.mp4

## الطريقة الأسهل: اطلب من Claude

ارفع الفيديو في المحادثة واكتب ما تريده بكلامك، مثلاً:

> اعمل زوم سريع على الثانية 3 مع صوت ووش، واهتزاز مع بوم عند الثانية 8، وحط فلتر سينمائي ولمعات في النهاية.

> ادمج هالثلاث مقاطع بانتقالات سلايد مع صوت ووش لكل انتقال.

## محتويات المجلد

| المجلد | المحتوى | الاستخدام في برامج المونتاج |
|---|---|---|
| `sfx/` | مؤثرات صوتية WAV | اسحبها مباشرة لأي برنامج |
| `luts/` | فلاتر ألوان `.cube` | CapCut: Adjust → LUT · Premiere: Lumetri → Creative → Look · DaVinci: LUTs |
| `overlays/` | طبقات ضوئية MP4 على خلفية سوداء | ضعها فوق الفيديو واختر وضع الدمج **Screen** |
| `previews/` | صور معاينة وفيديو تجريبي | — |
| `kit/` | الكود الذي يولّد كل شيء | — |
| `edit.py` | أداة تطبيق كل شيء على الفيديو | — |

## 🎥 الحركات والمؤثرات (`--fx`)

كل مؤثر يأخذ `t=` (وقت البداية) و `d=` (المدة) وخياراته الخاصة. المؤثرات التي تتبع نقطة تقبل أيضاً `x=` و `y=` (من 0 إلى 1) لتحديد مركزها.

| الاسم | النوع | الوصف | الخيارات الافتراضية |
|---|---|---|---|
| `zoom-punch` | حركة | زوم سريع على لحظة مهمة | `amount=1.25`, `speed=0.12`, `back=1`, `d=1.0` |
| `zoom-in` | حركة | زوم داخل بطيء | `amount=1.3`, `d=3.0` |
| `zoom-out` | حركة | زوم خارج بطيء | `amount=1.3`, `d=3.0` |
| `ken-burns` | حركة | زوم مع تحريك (للصور) | `amount=1.2`, `pan=1.0`, `d=5.0` |
| `shake` | حركة | اهتزاز الكاميرا | `amount=1.0`, `rotate=1.0`, `seed=1`, `d=0.8` |
| `earthquake` | حركة | اهتزاز قوي (زلزال) | `amount=1.0`, `rotate=1.0`, `seed=2`, `d=1.0` |
| `handheld` | حركة | كاميرا محمولة باليد | `amount=1.0`, `rotate=1.0`, `seed=3`, `d=5.0` |
| `pulse` | حركة | نبض مع الإيقاع | `amount=1.06`, `bpm=120`, `d=4.0` |
| `bounce` | حركة | ارتداد | `amount=1.12`, `d=1.0` |
| `tilt` | حركة | ميلان الكاميرا | `angle=8.0`, `back=1`, `d=2.0` |
| `slide-in` | حركة | دخول من جانب | `speed=0.35`, `from=left`, `d=0.5` |
| `spin` | انتقال | لفّة كاملة (تخفي القطع) | `turns=1.0`, `dir=1`, `d=0.6` |
| `whip` | انتقال | سحبة سريعة (Whip Pan) | `amount=1.0`, `dir=1`, `vertical=0`, `d=0.35` |
| `zoom-transition` | انتقال | زوم عبور بين لقطتين | `amount=2.5`, `d=0.5` |
| `flash` | انتقال | فلاش | `color=white`, `amount=1.0`, `d=0.4` |
| `dip` | انتقال | غمق ورجوع | `color=black`, `d=0.6` |
| `fade-in` | انتقال | ظهور تدريجي | `color=black`, `d=1.0` |
| `fade-out` | انتقال | اختفاء تدريجي | `color=black`, `d=1.0` |
| `impact` | ضربة | زوم+اهتزاز+فلاش للحظة قوية | `amount=1.3`, `rotate=1.0`, `seed=5`, `d=0.5` |
| `glitch` | رقمي | غلتش | `amount=1.0`, `seed=0`, `d=0.5` |
| `rgb-split` | رقمي | انفصال ألوان | `amount=1.0`, `d=1.0` |
| `vhs` | رقمي | شريط VHS قديم | `amount=1.0`, `d=3.0` |
| `strobe` | ضوء | ستروب | `rate=8.0`, `color=black`, `amount=0.8`, `d=1.0` |
| `light-sweep` | ضوء | لمعة تعبر الشاشة | `color=white`, `amount=0.5`, `d=0.8` |
| `glow` | ضوء | توهج للمناطق المضيئة | `amount=0.8`, `threshold=0.6`, `d=2.0` |
| `vignette` | ضوء | تعتيم الأطراف | `amount=0.6`, `d=3.0` |
| `bw` | لون | أبيض وأسود مؤقت | `d=2.0` |
| `invert` | لون | عكس الألوان | `d=0.1` |
| `tint` | لون | صبغة لونية | `color=cyan`, `amount=0.6`, `d=2.0` |
| `film` | لون | فيلم قديم (اهتزاز وارتعاش) | `amount=1.0`, `d=3.0` |
| `blur` | تمويه | تمويه | `amount=1.0`, `d=2.0` |
| `blur-in` | تمويه | من ضبابي لواضح | `amount=1.0`, `d=0.8` |
| `blur-out` | تمويه | من واضح لضبابي | `amount=1.0`, `d=0.8` |
| `zoom-blur` | تمويه | تمويه زوم | `amount=1.0`, `d=0.5` |
| `pixelate` | تمويه | تقطيع بكسل (إخفاء) | `w=1.0`, `h=1.0`, `block=3.0`, `d=2.0` |
| `blur-region` | تمويه | تمويه منطقة (إخفاء وجه/رقم) | `w=0.3`, `h=0.4`, `amount=1.0`, `d=2.0` |
| `mirror` | تشويه | مرآة | `d=2.0` |
| `wave` | تشويه | تموج (حلم/دوخة) | `amount=1.0`, `d=2.0` |
| `bulge` | تشويه | انتفاخ عدسة | `amount=1.0`, `d=1.5` |
| `echo` | تشويه | صدى حركة (أثر) | `amount=0.7`, `frames=8`, `d=2.0` |
| `letterbox` | سينمائي | أشرطة سينمائية متحركة | `ratio=2.35`, `back=1`, `d=4.0` |
| `freeze` | سينمائي | تجميد اللقطة | `bw=0`, `zoom=1.0`, `d=1.5` |

## 🔀 الانتقالات بين المقاطع (`join`)

`fade` · `fadeblack` · `fadewhite` · `dissolve` · `wipeleft` · `wiperight` · `wipeup` · `wipedown` · `slideleft` · `slideright` · `slideup` · `slidedown` · `smoothleft` · `smoothright` · `smoothup` · `smoothdown` · `circleopen` · `circleclose` · `circlecrop` · `rectcrop` · `vertopen` · `vertclose` · `horzopen` · `horzclose` · `radial` · `pixelize` · `zoomin` · `hblur` · `fadegrays` · `distance` · `diagtl` · `diagtr` · `diagbl` · `diagbr` · `hlslice` · `hrslice` · `vuslice` · `vdslice` · `squeezeh` · `squeezev` · `wipetl` · `wipetr` · `wipebl` · `wipebr` · `hlwind` · `hrwind` · `vuwind` · `vdwind` · `coverleft` · `coverright` · `coverup` · `coverdown` · `revealleft` · `revealright` · `revealup` · `revealdown`

**اختصارات:** `flash`→`fadewhite` · `black`→`fadeblack` · `white`→`fadewhite` · `zoom`→`zoomin` · `blur`→`hblur` · `slide`→`slideleft` · `wipe`→`wipeleft` · `circle`→`circleopen` · `pixel`→`pixelize` · `push`→`slideleft` · `cross`→`dissolve` · `gray`→`fadegrays` · `wind`→`hlwind` · `random` (انتقال عشوائي لكل قطع)

> للانتقال داخل فيديو واحد عند نقطة قطع، استخدم مؤثرات: `zoom-transition` · `whip` · `spin` · `flash` · `glitch` · `dip`

## 🔊 المؤثرات الصوتية (`--sfx`)

**انتقالات:** `whoosh-short` ووش قصير · `whoosh-long` ووش طويل · `whoosh-deep` ووش عميق بباص · `whoosh-double` ووش مزدوج · `whoosh-reverse` ووش يتصاعد وينقطع · `swoosh-fast` سووش سريع · `swish-air` هواء خفيف · `whip` ضربة سوط سريعة · `zoom-in` صوت زوم داخل · `zoom-out` صوت زوم خارج · `swipe` سحب سريع

**ضربات:** `impact-boom` بوم سينمائي · `cinematic-hit` ضربة سينمائية معدنية · `bass-drop` باص دروب · `sub-drop` هبوط باص عميق · `thud` ضربة مكتومة · `punch` لكمة · `slam` ضربة قوية · `braam` برااام سينمائي (ترايلر) · `vine-boom` بوم الميمز

**تصاعد:** `riser-tension` تصاعد توتر 3 ثواني · `riser-short` تصاعد قصير · `downlifter` هبوط تدريجي · `reverse-cymbal` صنج معكوس · `crash` صنج كراش · `drum-roll` قرع طبول مع ضربة

**واجهات:** `pop` بوب · `bubble-pop` فقاعة · `click` نقرة · `mouse-click` كبسة ماوس · `tick` تك · `toggle` مفتاح تشغيل · `notification` تنبيه · `message` رسالة واصلة · `success` نجاح · `error` خطأ · `coin` عملة (ألعاب) · `level-up` ليفل أب (ألعاب) · `correct` إجابة صحيحة · `wrong-buzzer` إجابة خاطئة

**رقمي:** `glitch-1` غلتش · `glitch-2` غلتش طويل · `glitch-short` غلتش قصير · `static` تشويش · `data-beeps` بيانات تقنية · `bleep` صفير حجب الكلام · `countdown` عد تنازلي 3-2-1 · `laser` ليزر · `power-up` تشغيل · `power-down` إطفاء · `camera-flash` فلاش كاميرا

**كرتون:** `boing` بوينغ · `slide-up` صفارة صاعدة · `slide-down` صفارة نازلة · `cartoon-pop` فلينة · `spring` زنبرك · `sad-trombone` ترومبون حزين (فشل) · `meme-bruh` نغمة ميمز هابطة · `ta-da` تا-دا

**واقعية:** `camera-shutter` غالق كاميرا · `typing` كتابة على كيبورد · `typewriter-ding` جرس آلة كاتبة · `heartbeat` نبض قلب · `clock-tick` تكتكة ساعة · `cash-register` كاشير (كا-تشينغ) · `record-scratch` خدش أسطوانة · `tape-stop` توقف شريط · `rewind` ترجيع · `vinyl-crackle` طقطقة أسطوانة قديمة · `footsteps` خطوات · `door-knock` طرق باب

**موسيقية:** `magic-shimmer` لمعة سحرية · `harp-gliss` هارب صاعد (حلم/ذكرى) · `dramatic-sting` دن دن دااان · `suspense-hit` ضربة غموض · `suspense-drone` خلفية توتر

**أجواء:** `wind` رياح · `rain` مطر · `crowd-cheer` تشجيع وتصفيق

## 🎨 فلاتر الألوان (`--lut`)

![فلاتر الألوان](previews/luts.jpg)

| الاسم | الوصف |
|---|---|
| `cinematic` | سينمائي متوازن |
| `teal-orange` | تركواز وبرتقالي (أفلام هوليوود) |
| `warm` | دافئ |
| `golden-hour` | ساعة ذهبية |
| `cool` | بارد |
| `moody` | مزاجي داكن |
| `film-fade` | فيلم باهت |
| `vintage` | قديم (فينتج) |
| `retro-80s` | ريترو الثمانينات |
| `sepia` | بني قديم |
| `bw` | أبيض وأسود |
| `noir` | أبيض وأسود عالي التباين |
| `cyberpunk` | سايبربانك |
| `neon-night` | ليل نيون |
| `pastel` | باستيل ناعم |
| `dreamy` | حالم |
| `sunset-pink` | غروب وردي |
| `vibrant` | ألوان حيوية |
| `punch` | تباين قوي |
| `bleach-bypass` | بليتش (أفلام حرب/أكشن) |
| `matrix` | أخضر ماتريكس |
| `kodak` | فيلم كوداك |
| `fuji` | فيلم فوجي |
| `desert` | صحراوي |
| `arctic` | قطبي بارد |
| `horror` | رعب |
| `cross-process` | كروس بروسس |
| `insta-fade` | إنستغرام باهت |
| `day-for-night` | تحويل النهار لليل |

يمكن تخفيف قوة الفلتر: `--lut cinematic,strength=0.6`

## ✨ الطبقات الضوئية (`--overlay`)

![الطبقات](previews/overlays.jpg)

| الاسم | الوصف |
|---|---|
| `leak-warm` | تسريب ضوء دافئ |
| `leak-golden` | تسريب ضوء ذهبي |
| `leak-red` | تسريب ضوء أحمر |
| `leak-blue` | تسريب ضوء أزرق |
| `leak-rainbow` | تسريب ضوء ملون |
| `lens-flare` | وهج عدسة يعبر الشاشة |
| `light-rays` | أشعة ضوء |
| `sparkles` | لمعات |
| `bokeh` | بوكيه (دوائر ضوء ضبابية) |
| `stars` | نجوم تتلألأ |
| `snow` | ثلج |
| `rain` | مطر |
| `embers` | جمر متطاير |
| `confetti` | قصاصات احتفال |
| `hearts` | قلوب طائرة |
| `dust` | غبار وخدوش فيلم قديم |
| `vhs` | VHS شريط فيديو قديم |
| `film-burn` | حرق فيلم (انتقال) |
| `fog` | ضباب |
| `lightning` | برق وعاصفة |

خيارات: `t=` `d=` `opacity=` — تدخل وتخرج بنعومة تلقائياً.

## ⌨️ الاستخدام اليدوي

```bash
pip install -r montage-kit/requirements.txt   # ويلزم ffmpeg

# عرض كل شيء متوفر
python3 montage-kit/edit.py list
python3 montage-kit/edit.py list sfx

# تطبيق مؤثرات على فيديو
python3 montage-kit/edit.py apply in.mp4 out.mp4 \
  --fx "zoom-punch,t=3,d=1.5" \
  --fx "shake,t=8,d=0.6" --sfx "impact-boom,t=8" \
  --sfx "whoosh-short,t=2.9" \
  --overlay "leak-warm,t=0,d=4,opacity=0.7" \
  --sticker "arrow,t=10,pos=top-right" \
  --lut cinematic --grain 0.3 --vignette 0.5 \
  --music song.mp3,vol=0.25,duck=1

# دمج مقاطع بانتقالات وصوت ووش
python3 montage-kit/edit.py join a.mp4 b.mp4 c.mp4 out.mp4 --transition slideleft --td 0.5 --whoosh
```

| خيار عام | المعنى |
|---|---|
| `--lut NAME,strength=` | فلتر ألوان على كامل الفيديو (أو مسار ملف .cube خاص بك) |
| `--grain 0-1` | حبيبات فيلم |
| `--vignette 0-1` | تعتيم الأطراف |
| `--sharpen 0-1` | زيادة الحدة |
| `--music FILE,vol=,duck=1,start=` | موسيقى خلفية تنخفض تلقائياً عند الكلام |
| `--voice 1.0` | مستوى صوت الفيديو الأصلي |
| `--sticker` | ستيكر نيون (نفس صيغة `overlay.py` في المجلد الرئيسي) |

## إعادة توليد الملفات

```bash
python3 montage-kit/generate.py            # الكل
python3 montage-kit/generate.py sfx boing  # عنصر محدد
```

لإضافة مؤثر جديد: أضف دالته في الملف المناسب داخل `kit/` وسجّله في القاموس أسفل الملف.

</div>
