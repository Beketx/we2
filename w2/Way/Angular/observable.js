class NewsPaper {
	constructor(name) {
		this.name = name
	}

	publishNews(news) {
		console.log(this.name + ' : ' + news)
	}

}

// const TengriNews = new NewsPaper( 'TengriNews');
// TengriNews.publishNews( 'Shcok kontent')

class SportObservable {
	constructor(){
		this.subscribers = []
	}
	subscribe(sub){
		this.subscribers.push(sub)
	}
	unsubscribe(exsub){
		this.subscribers = this.subscribers.filter(sub => sub!==exsub)
	}
	notify(news){
		// this.subscribers.foreach(function (NewsPaper){
		// 	NewsPaper.publishNews(news)
		// })
		this.subscribers.forEach(sub => {
			
			sub.publishNews(news)});
	}
}

const tengri = new NewsPaper('Tengri');
const newYork = new NewsPaper('York');
const alpha = new NewsPaper('alpha');

const sportInfo = new SportObservable();

sportInfo.subscribe(tengri)
sportInfo.subscribe(newYork)
sportInfo.subscribe(alpha)

sportInfo.unsubscribe(newYork)

sportInfo.notify('CriRo create his own car')