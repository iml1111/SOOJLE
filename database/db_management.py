from bson.objectid import ObjectId
from bson.json_util import loads, dumps
from datetime import datetime, timedelta
import numpy
#####################################
from global_func import *
import global_func
#####################################
from variable import *

#사용자 관련#############################################
#전체 유저 목록 반환
def find_all_user(db, _id=None, user_id=None, user_name=None, user_major=None, auto_login=None, topic=None, tag=None, fav_list=None, view_list=None, search_list=None, ft_vector=None, tag_sum=None, newsfeed_list=None):
	
	show_dict = {'_id': 0}
	if _id is not None: 
		show_dict['_id'] = 1
	if user_id is not None:
		show_dict['user_id'] = 1
	if user_name is not None:
		show_dict['user_name'] = 1
	if user_major is not None:
		show_dict['user_major'] = 1
	if topic is not None:
		show_dict['topic'] = 1
	if tag is not None:
		show_dict['tag'] = 1
	if tag_sum is not None:
		show_dict['tag_sum'] = 1
	if ft_vector is not None:
		show_dict['ft_vector'] = 1
	if fav_list is not None:
		show_dict['fav_list'] = 1
	if view_list is not None:
		show_dict['view_list'] = 1
	if search_list is not None:
		show_dict['search_list'] = 1
	if newsfeed_list is not None:
		show_dict['newsfeed_list'] = 1
	if auto_login is not None:
		show_dict['auto_login'] = 1

	result = db['user'].find({}, show_dict)

	return result

#특정 유저, 특정 필드 목록 반환
def find_user(db, _id=None, user_id=None, user_pw=None, user_name=None, user_major=None, auto_login=None, topic=None, tag=None, fav_list=None, view_list=None, search_list=None, ft_vector=None, tag_sum=None, newsfeed_list=None):
	
	show_dict = {'_id': 0}
	if _id is not None:
		show_dict['_id'] = 1
	if user_id is not None:
		show_dict['user_id'] = 1
	if user_pw is not None:
		show_dict['user_pw'] = 1
	if user_name is not None:
		show_dict['user_name'] = 1
	if user_major is not None:
		show_dict['user_major'] = 1
	if topic is not None:
		show_dict['topic'] = 1
	if tag is not None:
		show_dict['tag'] = 1
	if tag_sum is not None:
		show_dict['tag_sum'] = 1
	if ft_vector is not None:
		show_dict['ft_vector'] = 1
	if fav_list is not None:
		show_dict['fav_list'] = 1
	if view_list is not None:
		show_dict['view_list'] = 1
	if search_list is not None:
		show_dict['search_list'] = 1
	if newsfeed_list is not None:
		show_dict['newsfeed_list'] = 1
	if auto_login is not None:
		show_dict['auto_login'] = 1

	result = db['user'].find_one(
		{
			'user_id': user_id
		}, 
		show_dict)

	return result

#유저 생성
def insert_user(db, user_id, user_pw, user_name, user_major):
	topic_temp = numpy.ones(26)
	topic = (topic_temp / topic_temp.sum()).tolist()

	ft_vector = (numpy.zeros(30)).tolist()
	tag = {}
	tag_sum = 1
	fav_list = []
	view_list = []
	newsfeed_list = []
	search_list = []
	auto_login = 1

	result = db['user'].insert(
		{
			'user_id': user_id,
			'user_pw': user_pw,
			'user_name': user_name,
			'user_major': user_major,
			'ft_vector': ft_vector,
			'tag': tag,
			'tag_sum': tag_sum,
			'topic': topic,
			'fav_list': fav_list,
			'view_list': view_list,
			'newsfeed_list': newsfeed_list,
			'search_list': search_list,
			'auto_login': auto_login
		})

	return "success"

#유저 삭제
def remove_user(db, user_id):
	db['user'].remove(
		{
			'user_id': user_id
		}
	)

	return "success"

#유저 fav_list 중복 체크용
def check_user_fav_list(db, _id, post_obi):
	result = db['user'].find_one(
		{
			'_id': _id
		}, 
		{
			'fav_list': 
			{
				'$elemMatch': 
				{
					'_id': post_obi
				}
			}
		}
	)

	return result
#유저 fav_list에 요소 추가
def update_user_fav_list_push(db, _id, fav_obj):
	db['user'].update(
		{
			'_id': _id
		},
		{
			'$push': 
			{
				'fav_list': 
				{
					'$each': [fav_obj],
					'$position': 0
				}
			}
		}
	)
	return "success"
#유저 fav_list에 요소 삭제 (좋아요 취소한 경우)
def update_user_fav_list_pull(db, _id, post_obi):
	db['user'].update(
		{
			'_id': _id
		},
		{
			'$pull': 
			{
				'fav_list': 
				{
					'_id': post_obi
				}
			}
		}
	)
	return "success"
#유저 fav_list 갱신
def refresh_user_fav_list(db, user_id, refresh_obj_list):
	#fav_list 삭제
	db['user'].update(
		{
			'user_id': user_id
		},
		{
			'$unset': {'fav_list': 1}
		}
	)

	#새로운 fav_list 등록
	db['user'].update(
		{
			'user_id': user_id
		},
		{
			'$push': 
			{
				'fav_list':
				{
					'$each': refresh_obj_list,
					'$position': 0
				}
			}
		}
	)

	return "success"

#유저 view_list에 요소 추가
def update_user_view_list_push(db, _id, view_obj):
	db['user'].update(
		{
			'_id': _id
		},
		{
			'$push': 
			{
				'view_list':
				{
					'$each': [view_obj],
					'$position': 0
				}
			}
		}
	)
	return "success"
#유저 view_list 갱신
def refresh_user_view_list(db, user_id, refresh_obj_list):
	#view_list 삭제
	db['user'].update(
		{
			'user_id': user_id
		},
		{
			'$unset': {'view_list': 1}
		}
	)

	#새로운 view_list 등록
	db['user'].update(
		{
			'user_id': user_id
		},
		{
			'$push': 
			{
				'view_list':
				{
					'$each': refresh_obj_list,
					'$position': 0
				}
			}
		}
	)

	return "success"

#유저 search_list에 요소 추가
def update_user_search_list_push(db, user_id, search_obj):
	db['user'].update(
		{
			'user_id': user_id
		},
		{
			'$push': 
			{
				'search_list': 
				{
					'$each': [search_obj],
					'$position': 0
				}
			}
		}
	)
	return "success"
#유저 search_list 갱신
def refresh_user_search_list(db, user_id, refresh_obj_list):
	#search_list 삭제
	db['user'].update(
		{
			'user_id': user_id
		},
		{
			'$unset': {'search_list': 1}
		}
	)

	#새로운 view_list 등록
	db['user'].update(
		{
			'user_id': user_id
		},
		{
			'$push': 
			{
				'search_list':
				{
					'$each': refresh_obj_list,
					'$position': 0
				}
			}
		}
	)

	return "success"

#유저 newsfeed_list에 요소 추가
def update_user_newsfeed_list_push(db, _id, newsfeed_obj):
	db['user'].update(
		{
			'_id': _id
		},
		{
			'$push': 
			{
				'newsfeed_list':
				{
					'$each': [newsfeed_obj],
					'$position': 0
				}
			}
		}
	)
	return "success"
#유저 newsfeed_list 갱신
def refresh_user_newsfeed_list(db, user_id, refresh_obj_list):
	#newsfeed_list 삭제
	db['user'].update(
		{
			'user_id': user_id
		},
		{
			'$unset': {'newsfeed_list': 1}
		}
	)

	#새로운 view_list 등록
	db['user'].update(
		{
			'user_id': user_id
		},
		{
			'$push': 
			{
				'newsfeed_list':
				{
					'$each': refresh_obj_list,
					'$position': 0
				}
			}
		}
	)

	return "success"

#유저 오토로그인 변경
def update_user_auto_login(db, user_id, value):
	db['user'].update(
		{
			'user_id': user_id
		}, 
		{
			'$set': {'auto_login': value}
		}
	)

	return "success"

#뉴스피드 관련############################################
#토픽별 뉴스피드 타입 전체 반환
def find_all_newsfeed_of_topic(db):
	result = db['newsfeed_of_topic'].find(
		{
		}, 
		{
			'_id': 0
		}
	)
	return result

#토픽별 뉴스피드 타입 반환
def find_newsfeed_of_topic(db, newsfeed_name):
	result = db['newsfeed_of_topic'].find_one(
		{
			'newsfeed_name': newsfeed_name
		}, 
		{
			'_id': 0
		}
	)
	return result

#토빅별 뉴스피드 타입 여러개 반환
def find_newsfeed_of_topics(db, newsfeed_list):
	result = db['newsfeed_of_topic'].find(
			{
				'$or': newsfeed_list
				
			}, 
			{
				'_id': 0,
				'info': 1
			}
		)
	return result

#토픽별 뉴스피드 타입에 따른 뉴시피드 게시글들 반환
def find_newsfeed(db, info, tag, negative_tag, num):
	result = db[SJ_DB_POST].find(
		{
			'$and':
			[
				{'info': {'$regex': info}},
				{'tag': {'$nin': negative_tag}},
				{'tag': {'$in': tag}}
			]
		},
		{
			'_id': 1,
			'title': 1,
			'date': 1,
			'img': 1,
			'fav_cnt': 1,
			'url': 1,
			'title_token': 1,
			'info': 1,
			'tag': 1
		}
		).sort([('date', -1)]).limit(num)
	return result

#인기 뉴스피드 반환
def find_popularity_newsfeed(db, num):
	result = db[SJ_DB_POST].find(
		{}, 
		{
			'_id': 1,
			'title': 1,
			'date': 1,
			'img': 1,
			'fav_cnt': 1,
			'url': 1,
			'popularity': 1
		}
		).sort([('date', -1)]).limit(num).sort([('popularity', -1)])
	return result

#포스트 관련#############################################
#포스트 전체 가져오기
def find_all_posts(db, _id=None, title=None, date=None, post=None, tag=None, img=None, url=None, hashed=None, info=None, view=None, fav_cnt=None, title_token=None, token=None, topic=None, ft_vector=None, popularity=None, skip_=0, limit_=None):

	show_dict = {'_id': 0}

	if _id is not None:
		show_dict['_id'] = 1
	if title is not None:
		show_dict['title'] = 1
	if date is not None:
		show_dict['date'] = 1
	if post is not None:
		show_dict['post'] = 1
	if tag is not None:
		show_dict['tag'] = 1
	if img is not None:
		show_dict['img'] = 1
	if url is not None:
		show_dict['url'] = 1
	if hashed is not None:
		show_dict['hashed'] = 1
	if info is not None:
		show_dict['info'] = 1
	if view is not None:
		show_dict['view'] = 1
	if fav_cnt is not None:
		show_dict['fav_cnt'] = 1
	if title_token is not None:
		show_dict['title_token'] = 1
	if token is not None:
		show_dict['token'] = 1
	if topic is not None:
		show_dict['topic'] = 1
	if ft_vector is not None:
		show_dict['ft_vector'] = 1
	if popularity is not None:
		show_dict['popularity'] = 1

	if limit_ is None:
		#기본적으로 날짜순 정렬 (최신)
		result = db[SJ_DB_POST].find(
			{}, 
			show_dict
		).sort([('date', -1)]).skip(skip_)

	else:
		#기본적으로 날짜순 정렬 (최신)
		result = db[SJ_DB_POST].find(
			{}, 
			show_dict
		).sort([('date', -1)]).skip(skip_).limit(limit_)

	return result

#특정 포스트 가져오기 (가져오고 싶은 필드만 1로 지정하여 보내주면 됨)
def find_post(db, post_obi, _id=None, title=None, date=None, post=None, tag=None, img=None, url=None, hashed=None, info=None, view=None, fav_cnt=None, title_token=None, token=None, topic=None, ft_vector=None, popularity=None):

	show_dict = {'_id': 0}

	if _id is not None:
		show_dict['_id'] = 1
	if title is not None:
		show_dict['title'] = 1
	if date is not None:
		show_dict['date'] = 1
	if post is not None:
		show_dict['post'] = 1
	if tag is not None:
		show_dict['tag'] = 1
	if img is not None:
		show_dict['img'] = 1
	if url is not None:
		show_dict['url'] = 1
	if hashed is not None:
		show_dict['hashed'] = 1
	if info is not None:
		show_dict['info'] = 1
	if view is not None:
		show_dict['view'] = 1
	if fav_cnt is not None:
		show_dict['fav_cnt'] = 1
	if title_token is not None:
		show_dict['title_token'] = 1
	if token is not None:
		show_dict['token'] = 1
	if topic is not None:
		show_dict['topic'] = 1
	if ft_vector is not None:
		show_dict['ft_vector'] = 1
	if popularity is not None:
		show_dict['popularity'] = 1

	result = db[SJ_DB_POST].find_one(
		{
			'_id': ObjectId(post_obi)
		}, 
		show_dict
	)

	return result

def remove_post(db, post_obi):
	db[SJ_DB_POST].remove(
		{
			'_id': ObjectId(post_obi)
		}
	)

	return "success"

#포스트 좋아요
def update_post_like(db, post_obi):
	db[SJ_DB_POST].update(
		{
			'_id': ObjectId(post_obi)
		}, 
		{
			'$inc': {'fav_cnt': 1, 'popularity': 3}
		}
	)
	return "success"

#포스트 좋아요 취소
def update_post_unlike(db, post_obi):
	db[SJ_DB_POST].update_many(
		{
			'_id': ObjectId(post_obi)
		}, 
		{
			'$inc': 
			{
				'fav_cnt': -1, 
				'popularity': -3
			}
		}
	)
	return "success"

#포스트 조회수 올리기
def update_post_view(db, post_obi):
	db[SJ_DB_POST].update_one(
		{
			'_id': ObjectId(post_obi)
		}, 
		{
			'$inc': 
			{
				'view': 1, 
				'popularity': 1
			}
		}
	)

	return "success"

#검색 관련###############################################
#domain_title_regex 검색
def find_domain_title_regex(db, search_str):
	result = db['domain'].find(
			{
				'$or':
				[
					{'title': {'$regex':search_str}},
					{'url': {'$regex':search_str}}
				]
			}, 
			{
				'_id': 0,
				'title': 1,
				'post': 1,
				'url': 1
			}
		)
	return result

#domain_post_regex 검색
def find_domain_post_regex(db, regex_str):
	result = db['domain'].find(
			{
				'post': {'$regex':regex_str}
			}, 
			{
				'_id': 0,
				'title': 1,
				'post': 1,
				'url': 1
			}
		)
	return result

#post title regex 검색
def find_title_regex(db, search_str, type_check):
	return_dict = {
		'title':1,
		'date':1, 
		'img':1, 
		'url':1, 
		'fav_cnt': 1, 
		'title_token': 1, 
		'token': 1, 
		'tag': 1, 
		'popularity': 1,
		'ft_vector': 1
	}

	#priority
	if type_check == 0:
		result = db[SJ_DB_POST].find(
			{
				'title': {'$regex':search_str}
			}, 
			return_dict
		)

	#진로&구인
	elif type_check == 1:
		search_type = db['newsfeed_of_topic'].find_one(
			{
				'newsfeed_name': '진로&구인'
			}, 
			{
				'_id': 0,
				'info': 1
			}
		)
		info = "|".join(search_type['info'])

		result = db[SJ_DB_POST].find(
			{
				'$and':
				[
					{'title': {'$regex':search_str}},
					{'info': {'$regex': info}}
				]
			}, 
			return_dict
		)
	
	#공모전&행사 + 동아리&모임
	elif type_check == 2:
		search_type = db['newsfeed_of_topic'].find(
			{
				'$or':
				[
					{'newsfeed_name': '공모전&행사'},
					{'newsfeed_name': '동아리&모임'}
				]
			}, 
			{
				'_id': 0,
				'info': 1
			}
		)
		search_type = list(search_type)
		temp_list = search_type[0]['info'] + search_type[1]['info']
		info = "|".join(temp_list)

		result = db[SJ_DB_POST].find(
			{
				'$and':
				[
					{'title': {'$regex':search_str}},
					{'info': {'$regex': info}}
				]
			}, 
			return_dict
		)

	#나머지
	elif type_check == 3:
		search_type = db['newsfeed_of_topic'].find(
			{
				'$or':
				[
					{'newsfeed_name': '진로&구인'},
					{'newsfeed_name': '공모전&행사'},
					{'newsfeed_name': '동아리&모임'}
				]
			}, 
			{
				'_id': 0,
				'info': 1
			}
		)
		search_type = list(search_type)
		info = []
		
		for temp in search_type:
			info += temp['info']

		for i in info:
			if i[0] == '^':
				i = i[1:]
			if i[-1] == '$':
				i = i[:-1]

		info = '^(?!(' + "|".join(info) + '|everytime_))'

		result = db[SJ_DB_POST].find(
			{
				'$and':
				[
					{'title': {'$regex':search_str}},
					{'info': {'$regex': info}}
				]
			}, 
			return_dict
		)

	#커뮤니티
	else:
		result = db[SJ_DB_POST].find(
			{
				'$and':
				[
					{'title': {'$regex':search_str}},
					{'info': {'$regex': '^everytime_'}}
				]
				
			}, 
			return_dict
		)
	
	return result

#가상 post ids용 반환
def find_aggregate(db, tokenizer_list, type_check, limit_):
	now_time = datetime.now()

	project = {
		'$project':
		{
			'_id':1, 
			'title':1,
			'date':1,
			'img': 1,
			'url': 1,
			'fav_cnt': 1,
			'info': 1,
			###############
			'title_token':1,
			'token':1,
			'tag':1,
			'popularity':1,
			'ft_vector': 1
		}
	}
	addFields = {
		'$addFields':
		{
			'ids': 
			{
				'$divide':['$popularity', {'$subtract':[now_time, '$date']}]
			}
		}
	}
	sort = {
		'$sort': 
		{
			'ids': -1, 
			'date': -1
		}
	}
	limit = {'$limit': limit_}

	#priority
	if type_check == 0:
		result = db[SJ_DB_POST].aggregate([
			project, 
			{
				'$match': 
				{
					'token': {'$in': tokenizer_list}
				}
			}, 
			addFields, 
			sort, 
			limit
		])

	#진로&구인
	elif type_check == 1:
		search_type = db['newsfeed_of_topic'].find_one(
			{
				'newsfeed_name': '진로&구인'
			}, 
			{
				'_id': 0,
				'info': 1
			}
		)
		info = "|".join(search_type['info'])

		result = db[SJ_DB_POST].aggregate([
			project,
			{
				'$match': 
				{
					'$and': 
					[
						{'token': {'$in': tokenizer_list}},
						{'info': {'$regex': info}}
					]
				}
			},
			addFields,
			sort,
			limit
		])

	#공모전&행사 + 동아리&모임
	elif type_check == 2:
		search_type = db['newsfeed_of_topic'].find(
			{
				'$or':
				[
					{'newsfeed_name': '공모전&행사'},
					{'newsfeed_name': '동아리&모임'}
				]
			}, 
			{
				'_id': 0,
				'info': 1
			}
		)
		search_type = list(search_type)
		temp_list = search_type[0]['info'] + search_type[1]['info']
		info = "|".join(temp_list)

		result = db[SJ_DB_POST].aggregate([
			project,
			{
				'$match': 
				{
					'$and': 
					[
						{'token': {'$in': tokenizer_list}},
						{'info': {'$regex': info}}
					]
				}
			},
			addFields,
			sort,
			limit
		])

	#나머지
	elif type_check == 3:
		search_type = db['newsfeed_of_topic'].find(
			{
				'$or':
				[
					{'newsfeed_name': '진로&구인'},
					{'newsfeed_name': '공모전&행사'},
					{'newsfeed_name': '동아리&모임'}
				]
			}, 
			{
				'_id': 0,
				'info': 1
			}
		)
		search_type = list(search_type)
		info = []
		
		for temp in search_type:
			info += temp['info']

		for i in info:
			if i[0] == '^':
				i = i[1:]
			if i[-1] == '$':
				i = i[:-1]

		info = '^((?!' + "|".join(info) + '|everytime_).)*$'

		result = db[SJ_DB_POST].aggregate([
			project,
			{
				'$match': 
				{
					'$and': 
					[
						{'token': {'$in': tokenizer_list}},
						{'info': {'$regex': info}}
					]
				}
			},
			addFields,
			sort,
			limit
		])

	#커뮤니티
	else:
		result = db[SJ_DB_POST].aggregate([
			project,
			{
				'$match': 
				{
					'$and': 
					[
						{'token': {'$in': tokenizer_list}},
						{'info': {'$regex': '^everytime_'}}
					]
				}
			},
			addFields,
			sort,
			limit
		])

	return result

#full search title regex 검색
def find_full_title_regex(db, search_str, limit_):
	#priority	
	result = db[SJ_DB_POST].find(
		{
			'title': {'$regex':search_str}
		}, 
		{
			'title':1,
			'date':1, 
			'img':1, 
			'url':1, 
			'fav_cnt': 1, 
			'title_token': 1, 
			'token': 1, 
			'tag': 1, 
			'popularity': 1
		}
	).limit(limit_)
	return result

#full search post aggregate
def find_full_aggregate(db, tokenizer_list, limit_):
	now_time = datetime.now()
	
	result = db[SJ_DB_POST].aggregate([
		{
			'$project':
			{
				'_id':1, 
				'title':1,
				'date':1,
				'img': 1,
				'url': 1,
				'fav_cnt': 1,
				'info': 1,
				###############
				'title_token':1,
				'token':1,
				'tag':1,
				'popularity':1
			}
		},
		{
			'$match': 
			{
				'token': {'$in': tokenizer_list}
			}
		}, 
		{
			'$addFields':
			{
				'ids': 
				{
					'$divide':['$popularity', {'$subtract':[now_time, '$date']}]
				}
			}
		},
		{
			'$sort': 
			{
				'ids': -1, 
				'date': -1
			}
		}, 
		{'$limit': limit_}
	])

	return result

#title 토큰 검색
def find_title_token(db, token_list):
	result = db[SJ_DB_POST].find(
		{
			'title_token': {'$in': token_list}
		}, 
		{
			'_id':0, 
			'title':1, 
			'title_token': 1, 
			'data': 1
		}
	)
	return result

#token 검색
def find_token(db, token_list):
	result = db[SJ_DB_POST].find(
		{
			'token': {'$in': token_list}
		}, 
		{
			'_id':0, 
			'title':1, 
			'token': 1, 
			'data': 1
		}
	)
	return result

#logging####################################### 
#search_log에 search_obj 추가
def insert_search_log(db, user_id, split_list):
	db['search_log'].insert(
		{
			'user_id': user_id,
			'search_split': split_list,
			'date': datetime.now()
		}
	)
	return "success"

#search_log 가져온다.
def find_search_log(db):
	result = db['search_log'].find(
		{
			'date':
			{
				'$gte': global_func.get_default_day(1)
			}
		},
		{
			'_id': 0,
			'search_split': 1
		}
	).sort([('date', -1)])

	return result

#log에 기록!
def insert_log(db, user_id, url):
	db['log'].insert(
		{
			'user_id': user_id,
			'url': url,
			'date': datetime.now()
		}
	)
	return "success"

#log에서 시간별로 가져온다.
def find_date_log(db, date, limit_):
	result = db['log'].find(
		{
			'date':
			{
				'$gte': date
			}
		},
		{
			'_id': 0,
			'user_id': 1
		}
	).sort([('date', -1)]).limit(limit_)

	return result

#log에서 회원별로 가져온다.
def find_user_log(db, user_id, limit_):
	result = db['log'].find(
		{
			'user_id': user_id
		},
		{
			'_id': 0
		}
	).sort([('date', -1)]).limit(limit_)

	return result

#log에서 시간별 + 회원별로 가져온다.
def find_user_date_log(db, user_id, date, limit_):
	result = db['log'].find(
		{
			'$and':
			[
				{'date': {'$gte': date}},
				{'user_id': user_id}
			]
		},
		{
			'_id': 0
		}
	).sort([('date', -1)]).limit(limit_)

	return result

#pushback 함수
def insert_pushback(db, user_id, type_, back_obj_list):
	#좋아요 타입
	if type_ == 'fav':
		for back_obj in back_obj_list:
			db['pushback'].insert(
				{
					'user_id': user_id,
					'type': 'fav',
					'obj_id': back_obj['_id'],
					'topic': back_obj['topic'],
					'token': back_obj['token'],
					'tag': back_obj['tag'],
					'post_date': back_obj['post_date'],
					'title': back_obj['title'],
					'url': back_obj['url'],
					'img': back_obj['img'],
					'date': back_obj['date']
				}
			)
	
	#조회수 타입
	elif type_ == 'view':
		for back_obj in back_obj_list:
			db['pushback'].insert(
				{
					'user_id': user_id,
					'type': 'view',
					'obj_id': back_obj['_id'],
					'topic': back_obj['topic'],
					'token': back_obj['token'],
					'tag': back_obj['tag'],
					'post_date': back_obj['post_date'],
					'title': back_obj['title'],
					'url': back_obj['url'],
					'img': back_obj['img'],
					'date': back_obj['date']
				}
			)
	
	#검색 타입
	elif type_ == 'search':
		for back_obj in back_obj_list:
			db['pushback'].insert(
				{
					'user_id': user_id,
					'type': 'search',
					'original': back_obj['original'],
					'search_split': back_obj['search_split'],
					'tokenizer_split': back_obj['tokenizer_split'],
					'similarity_split': back_obj['similarity_split'],
					'date': back_obj['date']
				}
			)
	
	#뉴스피드 타입
	else:
		for back_obj in back_obj_list:
			db['pushback'].insert(
				{
					'user_id': user_id,
					'type': 'newsfeed',
					'newsfeed_name': back_obj['newsfeed_name'],
					'tag': back_obj['tag'],
					'date': back_obj['date']
				}
			)
		
	return "success"

#analysis######################################
#search_realtime 가져오기!
def find_search_all_realtime(db):
	result = db['search_realtime'].find(
		{},
		{
			'_id': 0
		}
	)
	return result

#admin#########################################
#공지사항 추가
def insert_notice(db, title, post, url):
	db['notice'].insert(
		{
			'title': title,
			'post': post,
			'url': url,
			'view': 0,
			'date': datetime.now(),
			'activation': 1
		}		
	)

	return "success"

#공지사항 수정
def update_notice(db, notice_obi, title, post, url):
	db['notice'].update(
		{
			'_id': ObjectId(notice_obi)
		},
		{
			'$set':
			{
				'title': title,
				'post': post,
				'url': url,
				'date': datetime.now()
			}	
		}
		
	)

	return "success"

#공지사항 삭제
def remove_notice(db, notice_obi):
	db['notice'].remove(
		{
			'_id': ObjectId(notice_obi)
		}
	)

	return "success"

#공지사항 전체 반환
def find_all_notice(db):
	result = db['notice'].find().sort([('date', -1)])

	return result

#공지사항 단일 반환
def find_notice(db, notice_obi):
	result = db['notice'].find_one(
		{
			'_id': ObjectId(notice_obi)
		}
	)

	return result

#게시글 추가
def insert_post(db, title, post, tag, img, url, info, hashed, url_hashed, token, view, fav_cnt, title_token, login, learn, popularity, topic, ft_vector):
	db['posts'].insert(
		{
			'title': title,
			'post': post,
			'tag': tag,
			'img': img,
			'url': url,
			'info': info,
			'hashed': hashed,
			'url_hashed': url_hashed,
			'token': token,
			'view': view,
			'fav_cnt': fav_cnt,
			'title_token': title_token,
			'login': login,
			'learn': learn,
			'popularity': popularity,
			'topic': topic,
			'ft_vector': ft_vector,
			'date': datetime.now()
		}
	)

	return "success"

#게시글 수정
def update_post(db, post_obi, title, post, tag, img, url, info, hashed, url_hashed, token, title_token, topic, ft_vector):
	db['posts'].update(
		{
			'_id': ObjectId(post_obi)
		},
		{
			'$set':
			{
				'title': title,
				'post': post,
				'tag': tag,
				'img': img,
				'url': url,
				'info': info,
				'hashed': hashed,
				'url_hashed': url_hashed,
				'token': token,
				'title_token': title_token,
				'topic': topic,
				'ft_vector': ft_vector
			}
		}
	)

	return "success"

#background ################################### 
#모든 유져를 불러온다. (관심도 측정용)
# def find_user_measurement(db, num):
# 	mongo_num = num * -1
# 	result = db['user'].find({}, {
# 		'fav_list': {'$slice': mongo_num}, 
# 		'view_list': {'$slice': mongo_num}, 
# 		'search_list': {'$slice': mongo_num},
# 		'newsfeed_list': {'$slice': mongo_num}
# 		})

# 	return result

#USER의 관심도 갱신.
def update_user_measurement(db, _id, topic, tag, tag_sum, ft_vector):
	db['user'].update({'_id': _id}, 
		{
			'$set': 
			{
				'topic': topic, 
				'tag': tag, 
				'tag_sum': tag_sum,
				'ft_vector': ft_vector
			}
		})

	return "success"

#search_realtime에 기록!
def insert_search_realtime(db, real_time_list):
	db['search_realtime'].insert(
		{
			'real_time' : real_time_list,
			'date': datetime.now()
		}
	)
	return "success"

#search_realtime 가져오기!
def find_search_realtime(db):
	result = db['search_realtime'].find(
		{},
		{
			'_id': 0,
			'real_time': 1,
			'date': 1
		}
	).sort([('date', -1)]).limit(1)
	return result

#제일 높은 좋아요 수 반환
def find_highest_fav_cnt(db):
	result = db[SJ_DB_POST].find_one(
		{
			'$query': {},
			'$orderby': {'fav_cnt': -1}
		},
		{
			'_id': 0,
			'fav_cnt': 1
		}
	)
	return result['fav_cnt']

#제일 높은 조회수 반환
def find_highest_view_cnt(db):
	result = db[SJ_DB_POST].find_one(
		{
			'$query': {},
			'$orderby': {'view': -1}
		},
		{
			'_id': 0,
			'view': 1
		}
	)
	return result['view']

#정적 테이블 변수 불러오기
def find_variable(db, key):
	result = db['variable'].find_one(
		{
			'key': key
		}, 
		{
			'_id': 0,
			'value':1
		}
	)
	return result['value']

#정적 테이블 변수 수정하기
def update_variable(db, key, value):
	db['variable'].update(
		{
			'key': key
		}, 
		{
			'$set': {'value': value }
		}
	)
	return "success"	

#좋아요/조회수 초기 셋팅용 더비 포스트 생성
def insert_dummy_post(db):
	topic_temp = numpy.ones(26)
	topic = (topic_temp / topic_temp.sum()).tolist()
	db[SJ_DB_POST].insert(
		{
			'title' : "(o^_^)o 안녕하세요. SOOJLE 입니다.",
			'date': get_default_day(10000),
			'post': "안녕하세요. SOOJLE 입니다.",
			'tag': [],
			'img': 1,
			'url': "",
			'hashed': "",
			'info': "SOOJLE",
			'view': 1,
			'fav_cnt': 1,
			'title_token': [],
			'token': [],
			'login': 0,
			'learn': 1,
			'popularity': 0,
			'fav_vector': (numpy.zeros(30)).tolist(),
			'topic': topic
		}
	)
	return "success"

def check_dummy_post(db):
	result = db[SJ_DB_POST].find_one({'title': "(o^_^)o 안녕하세요. SOOJLE 입니다."})

	return result
