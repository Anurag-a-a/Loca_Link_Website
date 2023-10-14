package com.team20.vcommunity.serviceImpl;

import com.team20.vcommunity.entity.User;
import com.team20.vcommunity.mapper.UserMapper;
import com.team20.vcommunity.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class UserServiceImpl implements UserService {

    @Autowired
    private UserMapper userMapper;

    @Override
    public User login(String username, String password) {
        return userMapper.getUser(username, password);
    }
}
