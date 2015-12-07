--readme: redis中使用keys 'bind_*'即可查询出block的ip
--白名单列表
white_list = {"101.231.117.66"}

--block列表
block_list = {{uri="/voiceMessage/sendVoiceSMS.html",limit_count=20,limit_timeout=300},{uri="/findPassword/checkVerifyCodeToStep2.html",limit_count=60,limit_timeout=60},{uri="/v5_mobile/mobile/user/checkMobile.html",limit_count=60,limit_timeout=60},{uri="/user/sendSMS.html",limit_count=30,limit_timeout=300}}

--block列表限制时间
ip_bind_time = 3600

local redis = require "resty.redis"
local cache = redis.new()
local ok,err = cache.connect(cache,"192.168.110.107","6379")

if not ok then
	goto A
end

--check sendSMS phone nubmer
if ngx.var.uri == "/user/sendSMS.html" then
        local m,smserr = ngx.re.match(ngx.var.request_uri,"phone=([0-9]{11}).*BUSICODE_REGISTER([0-9]{11})")
        if not m then
                ngx.log(ngx.ERR,"sendSMS_error: ",smserr)
        else
                local phone_no1 = m[1]
                local phone_no2 = m[2]
                if phone_no1 ~= phone_no2 then
                        ngx.exit(403)
                end
        end
end

if ngx.var.uri == '/findPassword/checkVerifyCodeToStep2.html' then
	mobile_no,err = ngx.req.get_uri_args()['mobileNo']
	if not mobile_no then
		goto A
	end
	is_bind,err = cache:get("bind_"..ngx.var.xxd_real_ip.."_"..mobile_no)
	if is_bind == "1" then
		ngx.exit(403)
		goto A
	end
	start_time,err = cache:get("time_"..ngx.var.xxd_real_ip.."_"..mobile_no)
	ip_count,err = cache:get("count_"..ngx.var.xxd_real_ip.."_"..mobile_no)
	if start_time == ngx.null or os.time() - tonumber(start_time) > 60 then
		res,err = cache:set("time_"..ngx.var.xxd_real_ip.."_"..mobile_no,os.time())
		res,err = cache:set("count_"..ngx.var.xxd_real_ip.."_"..mobile_no,1)
	else
		ip_count = ip_count + 1
		res,err = cache:incr("count_"..ngx.var.xxd_real_ip.."_"..mobile_no)
		if tonumber(ip_count) > 10 then
			local current_day = os.date("%Y-%m-%d",os.time())
			res,err = cache:set("bind_"..ngx.var.xxd_real_ip.."_"..mobile_no,1)
			res,err = cache:sadd("block_log","date:"..current_day..",".."ip:"..ngx.var.xxd_real_ip..",".."mobileNo:"..mobile_no.."uri:/findPassword/checkVerifyCodeToStep2.html")
		end
	end
end

for key in pairs(white_list) do
	--过滤白名单
	if ngx.var.xxd_real_ip == white_list[key] then
		goto A
	else
		for k,v in ipairs(block_list) do
			if ngx.var.uri == v.uri then
				--检测bind key,如果值为1返回403
				is_bind,err = cache:get("bind_"..ngx.var.xxd_real_ip.."_"..v.uri)
				if is_bind == "1" then
					ngx.exit(403)
					goto A
				end
				start_time,err = cache:get("time_"..ngx.var.xxd_real_ip.."_"..v.uri)
				ip_count,errr = cache:get("count_"..ngx.var.xxd_real_ip.."_"..v.uri)
				--超时
				if start_time == ngx.null or os.time() - tonumber(start_time) > v.limit_timeout then
					res,err = cache:set("time_"..ngx.var.xxd_real_ip.."_"..v.uri,os.time())
					res,err = cache:set("count_"..ngx.var.xxd_real_ip.."_"..v.uri,1)
				else
				--未超时
					ip_count = ip_count + 1
					res,err = cache:incr("count_"..ngx.var.xxd_real_ip.."_"..v.uri)
					--访问次数超出了限制,放入key为bind_且值为1
					if tonumber(ip_count) > v.limit_count then
						local current_day = os.date("%Y-%m-%d",os.time())
						res,err = cache:set("bind_"..ngx.var.xxd_real_ip.."_"..v.uri,1)
						--block日志记录,redis中以集合类型保存
						res,err = cache:sadd("block_log","date:"..current_day..",".."ip:"..ngx.var.xxd_real_ip..",".."uri:"..ngx.var.request_uri)
					end
				end
			end
		end
	end
end






::A::
local ok,err = cache:close()
