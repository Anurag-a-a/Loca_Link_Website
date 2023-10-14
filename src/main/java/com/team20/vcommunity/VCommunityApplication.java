package com.team20.vcommunity;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@MapperScan("com.team20.vcommunity.mapper")
public class VCommunityApplication {

    public static void main(String[] args) {
        SpringApplication.run(VCommunityApplication.class, args);
    }

}
