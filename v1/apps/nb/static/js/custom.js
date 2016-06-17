require.config({
	paths: {
		jquery: '/static/js/jquery.min',
		cookie: '/static/js/jquery.cookie',
		base: '/static/js/base',
		dom: '/static/js/dom',
		jfa: '/static/js/jfa',
	}
})

require(['jquery','base','jfa','cookie'], function($,Base,Jfa) {
	var Start = (function(){
		var _obj = {};
		return {
			getQuery : function(){
				log('data');
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
							//if(o.sval) location.href = '/analyze/?kwd='+urlencode(o.sval);
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