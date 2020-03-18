export interface Product{
  name: string,
  price: string, 
  rating: number,
  image: string,
  description: string,
  ref: string
}
export const products = [
  {
    name: 'IMICE, проводная, игровая мышь',
    price: 'US $7.91 - 9.89',
    rating: 4.6,
    image: "https://ae01.alicdn.com/kf/H8f5655b31ce4466bbecb74ae9107b3acC.jpg",
    description: 'IMICE, проводная, светодиодный, игровая мышь, 6 кнопок, 6400 dpi, USB, эргономичная, Mause, компьютерная мышь, геймер, с кабелем для ПК, ноутбука, RGB, оптическая мышьМышей с Подсветка',
    ref: 'https://aliexpress.ru/item/4000196649909.html?spm=a2g0o.detail.1000023.2.180bd2e7ptKvbp'
  },
  {
    name: 'Игровой коврик для мыши RGB',
    price: 'US $2.99 - 19.99',
    rating: 4.8,
    image: "https://ae01.alicdn.com/kf/HTB131wXKMHqK1RjSZFgq6y7JXXa8.jpg",
    description: 'Игровой коврик для мыши RGB большой коврик для мыши геймер большой коврик для мыши компьютерный Коврик Для Мыши Led подсветка XXL поверхность Mause коврик клавиатура Настольный коврик',
    ref: 'https://aliexpress.ru/item/32974466028.html?spm=a2g0o.detail.100009.4.3d812bf6upND8H&gps-id=pcDetailLeftTopSell&scm=1007.13482.95643.0&scm_id=1007.13482.95643.0&scm-url=1007.13482.95643.0&pvid=52550f90-de51-467a-ac8a-c0a90a7b4ed0&_t=gps-id:pcDetailLeftTopSell,scm-url:1007.13482.95643.0,pvid:52550f90-de51-467a-ac8a-c0a90a7b4ed0,tpp_buckets:668%230%23131923%2318_668%23808%234093%232_668%23888%233325%2318'
  },
  {
    name: 'USB 3,0 концентратор 2,0 концентратор',
    price: 'US $1.93 - 12.62',
    rating: 4.7,
    image: "https://ae01.alicdn.com/kf/Ha2863b31e2d641698e36257040ece744F.jpg",
    description: 'Спецификация блока питания составляет 3,5*1,35 мм  5 в 1 А, он поддерживает менее 1 ТБ жесткого диска, если ваш жесткий диск более 1 ТБ, то блок питания не подходит to   вам',
    ref: ''
  },
  {
    name: 'Xthree, оптовая продажа, брендовая Кепка',
    price: 'US $4.99',
    rating: 4.8,
    image: "https://ae01.alicdn.com/kf/HTB1BO_LLXXXXXbZXVXXq6xXFXXXM.jpg",
    description: 'Xthree, оптовая продажа, брендовая Кепка, бейсболка, облегающая Кепка, Повседневная Кепка, gorras, 5 панелей, хип-хоп, snapback, кепка для мужчин и женщин,<женщин> унисекс',
    ref: 'https://aliexpress.ru/item/32243608596.html?spm=a2g01.12602323.fdpcl001.1.7093753fZv6V4g&gps-id=5589723&scm=1007.23880.125255.0&scm_id=1007.23880.125255.0&scm-url=1007.23880.125255.0&pvid=fe26fcff-d25e-4d41-a02c-205d5b6706f2'
  },
  {
    name: 'Глобальная версия Xiaomi Redmi Note',
    price: 'US $169.00 - 188.00',
    rating: 4.9,
    image: "https://ae01.alicdn.com/kf/Hb75ff92e7a414041bab5e49d6dcbe383K.jpg",
    description: 'Язык: многоязычный,Хотите узнать больше о нескольких языках? Пожалуйста, нажмите здесьВопросы и ответы:Хотите узнать больше деталей о телефоне? Кликните здесь,',
    ref: 'https://aliexpress.ru/item/4000142909758.html?spm=a2g0o.productlist.0.0.117c1402YcZ6La&s=p&algo_pvid=2d117cdc-3880-42f3-ac65-59f7d9b6a2ca&algo_expid=2d117cdc-3880-42f3-ac65-59f7d9b6a2ca-1&btsid=0be3746c15814981653215036e7b8d&ws_ab_test=searchweb0_0,searchweb201602_,searchweb201603_'
  },
  {
    name: 'Xiaomi Redmi AirDots',
    price: 'US $17.99 - 22.59',
    rating: 4.8,
    image: "https://ae01.alicdn.com/kf/HTB1tIOJQgHqK1RjSZFEq6AGMXXab.jpg",
    description: 'Redmi AirDots оснащены 7,2 мм звуковым блоком, который обладает низкочастотным погружением и средне-высокой частотой. В компактном дизайне, мы все еще оснастили вас технологией DSP интеллектуального снижения шума окружающей среды',
    ref: 'https://aliexpress.ru/item/33001879444.html?spm=a2g0o.detail.100009.3.b8cb1b37p4Am9V&gps-id=pcDetailLeftTopSell&scm=1007.13482.95643.0&scm_id=1007.13482.95643.0&scm-url=1007.13482.95643.0&pvid=2aabcc61-a89c-4b59-8da4-bccba7c294b8&_t=gps-id:pcDetailLeftTopSell,scm-url:1007.13482.95643.0,pvid:2aabcc61-a89c-4b59-8da4-bccba7c294b8,tpp_buckets:668%230%23131923%2318_668%23808%234093%232_668%23888%233325%2318'
  },
  {
    name: 'Автомобильная dvr камера ',
    price: 'US $39.99 - 52.79',
    rating: 4.8,
    image: "https://ae01.alicdn.com/kf/Hb27ad3485c864dc8a062479a7111f20dm.jpg",
    description: ' Интеллектуальное Голосовое управление (Поддерживает только на английском языке)1920*1080 P Full HD, диафрагма 2,2 Высокочувствительный Датчик изображения sony IMX307 Поле зрения 130 ° ',
    ref: 'https://aliexpress.ru/item/32878227992.html?spm=a2g0o.detail.100009.5.60765e1cYU5aQ3&gps-id=pcDetailLeftTopSell&scm=1007.13482.95643.0&scm_id=1007.13482.95643.0&scm-url=1007.13482.95643.0&pvid=3e1c3fd2-b2f0-4f40-bbdc-c22ed0e6a7de&_t=gps-id:pcDetailLeftTopSell,scm-url:1007.13482.95643.0,pvid:3e1c3fd2-b2f0-4f40-bbdc-c22ed0e6a7de,tpp_buckets:668%230%23131923%2318_668%23808%234093%232_668%23888%233325%2318'
  },
  {
    name: 'Материнская плата для ПК',
    price: 'US $55.89',
    rating: 5.0,
    image: "https://ae01.alicdn.com/kf/H4f808a9211c047d193fbe674ea74e330r.jpg",
    description: 'Эта материнская плата используется, около 90% новая, 100% протестирована, она хорошо работает перед отправкой, и, возможно, без CMOS батареи для воздушного транспорта.',
    ref: 'https://aliexpress.ru/item/4000030260680.html?spm=a2g0v.best.6.9.5773UAxDUAxDk1&scm=1007.17258.160082.0&pvid=8b160adc-cdad-4374-91a3-45ac60558377'
  },
  {
    name: 'стекло для iPhone X XS',
    price: 'US $0.99 - 2.74',
    rating: 4.9,
    image: "https://ae01.alicdn.com/kf/HTB1cP80XRKw3KVjSZFOq6yrDVXaQ.jpg",
    description: '3 шт полное покрытие стекло для iPhone X XS Max XR закаленное стекло для iPhone 7 8 6 6s Plus 5 5S SE 11 Pro защита экрана3 шт полное покрытие стекло для iPhone X XS Max XR закаленное стекло',
    ref: 'https://aliexpress.ru/item/33022282524.html?spm=a2g0o.productlist.0.0.117c1402YcZ6La&algo_pvid=2d117cdc-3880-42f3-ac65-59f7d9b6a2ca&algo_expid=2d117cdc-3880-42f3-ac65-59f7d9b6a2ca-8&btsid=0be3746c15814981653215036e7b8d&ws_ab_test=searchweb0_0,searchweb201602_,searchweb201603_'
  }
  
 
];


/*
Copyright Google LLC. All Rights Reserved.
Use of this source code is governed by an MIT-style license that
can be found in the LICENSE file at http://angular.io/license
*/