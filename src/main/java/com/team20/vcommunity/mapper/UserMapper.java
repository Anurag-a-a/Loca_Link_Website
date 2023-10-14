package com.team20.vcommunity.mapper;

import com.team20.vcommunity.entity.User;

public interface UserMapper {

    User getUser(String username, String password);

}
