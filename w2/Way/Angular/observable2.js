class NewsPaper {
    constructor(name) {
        this.name = name
    }

    publishNews(news) {
        console.log(this.name + ' : ' + news)
    }
}

class SportNewsObservable {
    constructor() {
        this.subscrbers = []
    }

    subscribe(sub) {
        this.subscrbers.push(sub)
    }

    unsubscribe(exSub) {
        this.subscrbers = this.subscrbers.filter(sub => sub !== exSub)
    }

    notify(news) {
        this.subscrbers.forEach(function (newsPaper) {
            newsPaper.publishNews(news)
        })
    }
}

const tengriNews = new NewsPaper('tengriNews');
const newYorkTimes = new NewsPaper('newYorkTimes');
const zakonKz = new NewsPaper('zakonKz');

const sportInfo = new SportNewsObservable();

sportInfo.subscribe(tengriNews)
sportInfo.subscribe(newYorkTimes)
sportInfo.subscribe(zakonKz)

sportInfo.notify('Погиб Коби Брайан')

sportInfo.unsubscribe(zakonKz)

sportInfo.notify('Футбол больше не самый популярный(ШОК)')

let subs = {}

function addSub(newSub) {
    subs[newSub.name] = newSub
}


const forbes = {
    name: 'forbes',
    description: 'Fancy journal'
}

const tengri = {
    name: 'tengri',
    description: 'Fancy journal'
}

addSub(forbes)
addSub(tengri)

console.log(subs)