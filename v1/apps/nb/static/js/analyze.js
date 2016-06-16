require.config({
	paths: {
		jquery: '../js/jquery.min',
		cookie: '../js/jquery.cookie',
		base: '../js/base',
		jfa: '../js/jfa',
		drawe: '../js/drawe',
		echarts: '../js/echarts.min'
	}
})

require(['jquery','base','jfa','drawe','echarts','cookie'], function($,Base,Jfa,Dr,ec) {
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
						sbtn : function(o){
							if(o.sval) location.href = '/analyze/?kwd='+urlencode(o.sval);
						},
					}
				});
				Base.init({
					login : function(){
						_obj.getQuery();
					}
				});
				
			}
		}
	})();
	$(function() {
		Start.init()
	})
})