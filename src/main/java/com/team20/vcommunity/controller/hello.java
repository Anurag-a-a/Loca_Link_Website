package com.team20.vcommunity.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/")
public class hello {

    @RequestMapping("/")
    public String hello(){
        return "hello";
    }

}
