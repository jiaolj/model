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
			getQuery : function(){
				
			},
			user : {
				get : function(suc){
					$.ajax({
						url : '/user/get',
						success : function(back){
							suc && suc(back);
						}
					})
				},
				login : function(data,suc){
					$.ajax({
						url : '/user/login',
						data : data,
						success : function(back){
							suc && suc(back);
						}
					})
				},
				logout : function(suc){
					$.ajax({
						url : '/user/logout',
						success : function(back){
							suc && suc(back);
						}
					})
				},
				member : [
					{username:'1872',password:'123456',rank:'1'},
					{username:'udms',password:'udms',rank:'0'}
				],
				show : function(suc,arg){
					_obj.user.get(function(back){
						if(back.state=='ok'){
							suc && suc(back);
						}else{
							if(arg){
								Jfa.tools.login(function(){
									var uname = $('.msg.login input[name="username"]').val().trim(),
										passwd = $('.msg.login input[name="password"]').val().trim();
									_obj.user.login({uname:uname,passwd:passwd},function(back2){
										if(back2.state=='ok'){
											Jfa.tools.alertLeave();
											$('.msg.login p.error').text('登陆成功');
											$('nav.user>span').text(uname);
											$('nav.user>a.login').text('注销');
											$('nav.user>a.reg').text('');
											$('.jui-login-box').removeClass('hide');
											suc && suc();
										}else{
											$('.msg.login p.error').text('账号或密码错误');
										}
									})
								})
							}
						}
					})
				},
				bind : function(){
					$('nav.user>a').click(function(){
						var o = $(this),
							txt = o.text();
						if(txt=='登陆'){
							_obj.user.show(function(){
								_obj.getQuery();
							},1);
						}
						else if(txt=='注销'){
							_obj.user.logout(function(back){
								if(back.state=='ok') location.href = '';
							})
						}
					})
				}
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
							
						},
					}
				});
				Base.init();
				_obj.req = Jfa.tools.getRequest();
				_obj.user.bind();
				
				_obj.user.show(function(back){
					$('nav.user>span').text(back.data.uname);
					$('nav.user>a.login').text('注销');
					$('nav.user>a.reg').text('');
					_obj.getQuery();
				})
			}
		}
	})();
	$(function() {
		Start.init()
	})
})