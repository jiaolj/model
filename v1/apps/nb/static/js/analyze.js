require.config({
	paths: {
		dir : '/static/js/',
		jquery: '/static/js/jquery.min',
		cookie: '/static/js/jquery.cookie',
		base: '/static/js/base',
		jfa: '/static/js/jfa',
		dom: '/static/js/dom',
		drawe: '/static/js/drawe',
		echarts: '/static/js/ec/',
	}
})

require(['jquery','base','jfa','drawe','echarts','echarts/test','echarts/chart/line','echarts/chart/map','cookie'], function($,Base,Jfa,Dr) {
	var Start = (function(){
		var _obj = {};
		return {
			getLogin : function(){
				log('logging');
			},
			init : function(){
				_obj = this;
				_obj.conf = {
					page : {
						news : 1,
						f : 0,
						l : 10
					},
					tp : 'music',
				};
				Jfa.init({
					size:(100/1920),
					callback : {
						menu1 : function(o){
							log(o.text());
						},
					}
				});
				Base.init({
					login : function(){
						_obj.getLogin();
					}
				});
				Dr.getLine('lineChart').getMap('mapChart',[{name:'中国',value:100},{name:'美国',value:80}]);
			}
		}
	})();
	$(function() {
		Start.init()
	})
})