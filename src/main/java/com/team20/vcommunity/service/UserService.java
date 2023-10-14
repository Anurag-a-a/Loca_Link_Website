package com.team20.vcommunity.service;

import com.team20.vcommunity.entity.User;

public interface UserService {

    User login(String username, String password);

}
