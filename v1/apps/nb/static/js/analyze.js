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
			getTree : function(){
				_obj.conf.o.tree.html('\
					<dt s="0">\
						<a><b class="jsw"></b>地区</a><span class="jswitch" s="1"></span>\
						<dl class="json">\
							<dt s="0">\
								<a><b class="jsw"></b>中国</a><span class="jswitch" s="1"></span>\
								<dl class="json">\
									<dt s="0">\
										<a><b class="jsw"></b>北京</a><span class="jswitch" s="1"></span>\
									</dt>\
									<dt s="0">\
										<a><b class="jsw"></b>浙江</a><span class="jswitch" s="1"></span>\
									</dt>\
								</dl>\
							</dt>\
							<dt s="0">\
								<a><b class="jsw"></b>美国</a><span class="jswitch" s="1"></span>\
								<dl class="json">\
									<dt s="0">\
										<a><b class="jsw"></b>纽约</a><span class="jswitch" s="1"></span>\
									</dt>\
									<dt s="0">\
										<a><b class="jsw"></b>华盛顿</a><span class="jswitch" s="1"></span>\
									</dt>\
								</dl>\
							</dt>\
						</dl>\
					</dt>\
				').find('a').click(function(){
					var o = $(this),
						dt = o.parent(),
						s = Jfa.sw(dt,dt.attr('s'))
					;
				})
				_obj.conf.o.tree.find('span.jswitch').click(function(){
					var o = $(this),
						s = Jfa.sw(o,o.attr('s'))
					;
					o.parent().find('span.jswitch').attr('s',s);
				})
			},
			init : function(){
				_obj = this;
				_obj.conf = {
					o : {
						tree : $('#treeList'),
					},
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
						menu1 : function(o,ci){
							if(ci=='1'){
								Dr.getLine('lineChart').getMap('mapChart',[{name:'中国',value:100},{name:'美国',value:80}]);
							};
						},
					}
				});
				Base.init({
					login : function(){
						_obj.getLogin();
					}
				});
				_obj.getTree();
			}
		}
	})();
	$(function() {
		Start.init()
	})
})