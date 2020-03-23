$(function(){
    window.onerror=function(){return!0};
    $.cookie.raw = true;
    $.cookie.json = true;
	
	$(".search-submit").click(function(event) {
		$(this).removeAttr("name");
		event.preventDefault();
		var val = $.trim($(".search-title").val());
		if(val!==""){
			$(".search-window").find("form").submit();
			
		}else{
			alert("请输入关键词");
		}
		return false;
	});
	
	function filterDataImg(data, filter, num){
		if(data.length < 3){
			filter = [];
		}
		var _data = data.slice(0);
		var _dataImg = $.map(data, function(val, i){
			if(val.img&&$.inArray(i, filter)===-1)
				return i;
		});
		var id = 0;
		$.each(filter, function(index, j){
			if(!data[j].img){
				var temp = $.extend(true, {}, data[j]);
				if(_dataImg[id]){
					data[j] = _data[_dataImg[id]];
					data[_dataImg[id]] = temp;
					id++;
				}
			}
		});
		return data.slice(0,num);
	}
	
	function filterData(data,num,m){
		var items = new Array(num);
		var after = data.slice(m);
			$.each(items, function(index, val){	
				items[index] = index > 3 ? after[index-3] : data[index];
				
				if((index===0||index===3)&&!items[index].img){
						$.each(after, function(i, v){
							if(after[i].img){
								var temp = $.extend(true,{}, data[index]);
								items[index] = $.extend(true,{},after[i]);
								after[i] = temp;
								return false;
							}
						});
				}

			});
		return items;
	}
	
	function showxnxw(data, cookie){
		if(!data||!data.length)
			return;
		$(".xnxw").empty();
		var html = "<ul class=\"clearfix\">";
		$.each(data, function(index, val){
			var i = index%4;
			if(i===0){
				html += '<li class="news-box clearfix"><div class="qbox">';
			}
			if(val.img !== ""){
				//html +="<div class='news n"+index+" clearfix'><div class='slt' ><a href='"+val.link+"' target='_blank' title='"+val.title+"' ><div class='imgs' style='background-image:url("+val.img+")'></div></a></div><div class='bt'><a href='"+val.link+"' target='_blank' title='"+val.title+"'>"+val.title+"</a></div><div class='time'>"+val.date+"</div><div class='nr'><a href='"+val.link+"' target='_blank' title='"+val.abstract+"' >"+val.abstract+"</a></div></div>";  
				html +="<div class='news n"+index+" clearfix'><div class='slt pr'><a href='"+val.link+"' target='_blank' title='"+val.title+"'><div class='imgs' style='background-image:url("+val.img+")'></div></a><div class='bt'><a href='"+val.link+"' target='_blank' title='"+val.title+"'>"+val.title+"</a></div><div class='titlebg'></div></div><div class='time'>"+val.date+"</div><div class='nr'><a href='"+val.link+"' target='_blank' title='"+val.abstract+"' >"+val.abstract+"</a></div></div>";  
			}else{
				//html +="<div class='news n"+index+" clearfix'><div class='bt'><a href='"+val.link+"' target='_blank' title='"+val.title+"'>"+val.title+"</a></div><div class='time'>"+val.date+"</div><div class='nr'><a href='"+val.link+"' target='_blank' title='"+val.abstract+"' >"+val.abstract+"</a></div></div>";  
				html +="<div class='news n"+index+" clearfix'><div class='bt'><a href='"+val.link+"' target='_blank' title='"+val.title+"'>"+val.title+"</a></div><div class='time'>"+val.date+"</div><div class='nr'><a href='"+val.link+"' target='_blank' title='"+val.abstract+"' >"+val.abstract+"</a></div></div>";  
			}
			if(index&&i===0){ 
				if(index===data.length-1){
					html += '</div></li>';
				}
			}else{
				if(index===data.length-1){
					html += '</div></li>';
				}
			}
		});
		
		html +="</ul>";
		
		$(".xnxw").html(html);
		
		$(".zdy-2>ul").sudyScroll({
			width: 766,		
			height: 475,	
			display: 1,		
			step: 1,		
			dir:"x",		
			auto:false,		
			speed:500,		
			hoverPause:5000,		
			navigation:false,		
			navTrigger:"click", 	
			pagination:true,		
			pagTrigger:"mouseenter"  
		});
		
	}
	
	//////////
	function filterData1(data,num,m){
		if(data.length < 3){
			num = '';
		}
		var items = new Array(num);
			var after = data.slice(m);
			$.each(items, function(index, val){
				items[index] = data[index];
		});
		return items;
	}
	function showxysh1(data, cookie){
		if(!data||!data.length)
			return;
		$(".xysh1").empty();
		$.each(data,function(index, val){
			$(".xysh1").append("<li class='newsn n"+index+" clearfix'><p class='news_title'><a href='"+val.link+"' target='_blank' title='"+val.title+"' >"+val.title+"</a></p><p class='news_meta'><a href='"+val.link+"' target='_blank' title='"+val.abstract+"' >"+val.abstract+"</a></p></li>"); 
		});
		
	}
	
	/////////
	function showkxyj(data, cookie){
		if(!data||!data.length)
			return;
		$(".kxyj").empty();
		$.each(data,function(index, val){
			if(val.img !== ""){
				$(".kxyj").append("<li class='news n"+index+" clearfix'><div class='slt pr'><a href='"+val.link+"' target='_blank' title='"+val.title+"'><div class='imgs' style='background-image:url("+val.img+")'></div></a><div class='bt'><a href='"+val.link+"' target='_blank' title='"+val.title+"'>"+val.title+"</a></div><div class='titlebg'></div></div></li>");
			}else{
				$(".kxyj").append("<li class='news n"+index+" clearfix'><div class='bt'><a href='"+val.link+"' target='_blank' title='"+val.title+"'>"+val.title+"</a></div><div class='time'>"+val.date+"</div><div class='nr'><a href='"+val.link+"' target='_blank' title='"+val.abstract+"' >"+val.abstract+"</a></div></li>");  
			}

		})
	}

	showxnxw(filterDataImg(xnxw,[],8));
    showkxyj(filterDataImg(kxyj,[0,3],4));
	showxysh1(filterData1(xysh1,3,3));

	/*复制下拉*/
	$(".navbox .wp_nav > .nav-item").each(function(index,val){
		$(this).find("a").removeAttr("title");
		var html = $(this).find(".sub-nav").html();
		$(".navlist").append("<div class='navlist-li navlist-li-"+index+"'></div>");
		$(".navlist").find(".navlist-li").eq(index).html(html);
		$(".navlist").children(".navlist-li").find("ul").remove();
	});
	$(".navlist").append("<div class='clear'></div>");
	
	$(".navbar .nav-item:not(.i2)").click(function(){
	  $(".navlist").slideToggle("slow");
      return false;  
	});
	
	/*媒体链接*/
	$(".shares .share").each(function(){
		$(this).children("a").hover(function(){
			$(this).parent().find(".con").fadeIn();			
		},function(){
			$(this).parent().find(".con").fadeOut();
		});
	});
	
	$("body,html").click(function(){
		$(".search-window").animate({"width":"45px"});
		$(".searchbtn").stop(true,true).fadeIn();
		$(".navlist").slideUp();
	});
	
	$(".searchbtn").click(function(){
		$(this).stop(true,true).fadeOut();
		$(".search-window").stop(true,true).animate({"width":"200px"});
		return false;
	});	
	$(".search-input").click(function(){
		return false;
	});
	
	$(".kxbtn").hover(function(){
		$(".btncon").fadeIn();
	},function(){
		$(".btncon").fadeOut();
	});

	$(".site-logo").parent("a").attr("href","/main.htm");
	
	var href = $(".post-23").find("a").attr("href");
	var length = $(".post-22").find("li.newsn").length;
	$(".post-22").find("li.newsn").each(function(index,el){
	    if($(this).find("a").attr("href") == href){
			$(this).remove();
		}
	});
	if(length>2){
		$(".post-22").find("li.newsn").eq(2).remove();
		
	}

//$('#wp_news_w91 .sudy-scroll-wrap').rollNoInterval().left();


});