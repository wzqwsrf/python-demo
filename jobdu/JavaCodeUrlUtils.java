package com.wzq.test;
/**
 * @author:wangzq
 * @email:wangzhenqing1008@163.com
 * @date:2015-06-30 11:01:54
 * @description:将抓取的代码进行代码格式化
 */

import java.io.*;
import java.util.HashMap;
import java.util.Map;
import java.util.regex.Pattern;


public class JavaCodeUrlUtils {

    private static Map<String, String> articleMap = new HashMap<String, String>();

    /**
     * @param file
     * @return
     * @Description: 获取文件内容
     * @date 2013-7-11,下午04:30:48
     * @author wangzq
     * @version 3.0.0
     */
    public static String getFileCode(File file, String fileName) {
        fileName = fileName.substring(0, fileName.length() - 5);
        System.out.println(fileName);
        if (fileName.equals("题目1040：Prime Number")){
            System.out.println(111);
        }
        String code = "";
        try {
            String encoding = "utf-8";
            if (file.isFile() && file.exists()) { // 判断文件是否存在
                InputStreamReader read = new InputStreamReader(
                        new FileInputStream(file), encoding);// 考虑到编码格式
                BufferedReader bufferedReader = new BufferedReader(read);
                String lineTxt = null;
                while ((lineTxt = bufferedReader.readLine()) != null) {
                    code += lineTxt + "\n";
                    if (lineTxt.contains("@url:http://ac.jobdu.com/problem.php?pid")
                            && articleMap.containsKey(fileName)) {
                        System.out.println(fileName);

                        code += " * 解题思路参考csdn:" + articleMap.get(fileName) + "\n";
                    }
                }
                read.close();
            } else {
                System.err.println("找不到指定的文件");
            }
        } catch (Exception e) {
            System.err.println("读取文件内容出错");
            e.printStackTrace();
        }
        return code;
    }

    /**
     * 获取目录下的所有文件。
     *
     * @param path
     */
    public static void getDirectoryFiles(String path, String newPath) {
        File dirFile = new File(path);
        if (!dirFile.isDirectory()) {
            System.err.println(path + "不是文件夹，请检查!");
        }
        File[] files = dirFile.listFiles();
        for (File file : files) {
            String fileName = file.getName();
            String code = getFileCode(file, fileName);
            if ("".equals(code)) {
                System.out.println(fileName);
            }
//            System.out.println(code);
            writeCodeToFile(newPath + File.separator + fileName, code);
        }
    }

    /**
     * 将内容写入文件
     *
     * @param filePath
     * @param code
     */
    public static void writeCodeToFile(String filePath, String code) {
        try {
            File file = new File(filePath);
            PrintStream ps = new PrintStream(new FileOutputStream(file));
            ps.println(code);// 往文件里写入字符串
        } catch (FileNotFoundException e) {
            System.err.println("写文件内容出错");
            e.printStackTrace();
        }
    }

    /**
     * @param filename
     * @return
     * @Description: 获取博客日志信息
     * @date 2015-06-30 16:54:22
     * @author wangzq
     */
    public static void getCSDNArticles(String filename) {
        File file = new File(filename);
        try {
            String encoding = "utf-8";
            if (file.isFile() && file.exists()) { // 判断文件是否存在
                InputStreamReader read = new InputStreamReader(
                        new FileInputStream(file), encoding);// 考虑到编码格式
                BufferedReader bufferedReader = new BufferedReader(read);
                String lineTxt = null;
                while ((lineTxt = bufferedReader.readLine()) != null) {
                    lineTxt = lineTxt.trim();
                    String array[] = lineTxt.split(Pattern.quote("||"));
                    String head = "";
                    String url = array[1].trim();
                    if (array[0].contains("&&")) {
                        String headArr[] = array[0].split("&&");
                        for (int i = 0; i < headArr.length; i++) {
                            if (!headArr[i].contains("LeetCode")) {
                                head = headArr[i].replace("【九度】", "").trim();
                                articleMap.put(head, url);
                            }
                        }
                    } else if (array[0].contains("【九度】")) {
                        head = array[0].replace("【九度】", "").trim();
                        articleMap.put(head, url);
                    }
                }
                read.close();
            } else {
                System.err.println("找不到指定的文件");
            }
        } catch (Exception e) {
            System.err.println("读取文件内容出错");
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        String path = "/Users/wangzhenqing/git_work/java/test";
        String newPath = "/Users/wangzhenqing/git_work/java/new";
        getCSDNArticles("/Users/wangzhenqing/git_work/java/1.txt");
        System.out.println(articleMap.size());
        for (String head : articleMap.keySet()) {
            System.out.println(head);
            System.out.println(articleMap.get(head));
        }
        System.out.println(articleMap.get("题目1040：Prime Number"));
        getDirectoryFiles(path, newPath);
    }
}
