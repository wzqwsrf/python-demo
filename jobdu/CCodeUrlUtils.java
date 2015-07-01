package com.wzq.test;

/**
 * @author:wangzq
 * @email:wangzhenqing1008@163.com
 * @date:2015-06-30 11:01:54
 * @description:给C++增加头文件
 */

import java.io.*;
import java.util.HashMap;
import java.util.Map;
import java.util.regex.Pattern;


public class CCodeUrlUtils {

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
                }
                read.close();
            } else {
                System.err.println("找不到指定的文件c++文件");
            }
        } catch (Exception e) {
            System.err.println("读取c++文件内容出错");
            e.printStackTrace();
        }
        return code;
    }

    /**
     * 获取目录下的所有文件。
     *
     * @param path
     */
    public static void getDirectoryFiles(String path, String newPath,
                                         String cPath) {
        File dirFile = new File(path);
        if (!dirFile.isDirectory()) {
            System.err.println(path + "不是文件夹，请检查!");
        }
        File[] files = dirFile.listFiles();
        for (File file : files) {
            String fileName = file.getName();
            String head = getJavaHeadInfo(newPath + File.separator +
                    fileName.substring(0, fileName.length() - 4) + ".java");
            String code = getFileCode(file, fileName);
            code = head + code;
            if ("".equals(code)) {
                System.out.println(fileName);
            }
//            System.out.println(code);
            writeCodeToFile(cPath + File.separator + fileName, code);
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
     * @Description: 获取同文件名Java信息
     * @date 2015年06月30日18:27:18
     * @author wangzq
     */
    public static String getJavaHeadInfo(String filename) {
        String head = "";
        File file = new File(filename);
        try {
            String encoding = "utf-8";
            if (file.isFile() && file.exists()) { // 判断文件是否存在
                InputStreamReader read = new InputStreamReader(
                        new FileInputStream(file), encoding);// 考虑到编码格式
                BufferedReader bufferedReader = new BufferedReader(read);
                String lineTxt = null;
                int k = 0;
                while ((lineTxt = bufferedReader.readLine()) != null) {
                    if (k > 10) {
                        break;
                    }
                    head += lineTxt + "\n";
                    k++;
                }
                read.close();
            } else {
                System.err.println("找不到指定的Java文件" + filename);
            }
        } catch (Exception e) {
            System.err.println("读取Java文件内容出错");
            e.printStackTrace();
        }
        return head;
    }

    public static void main(String[] args) {
        String path = "/Users/wangzhenqing/git_work/java/test";
        String newPath = "/Users/wangzhenqing/git_work/java/new";
        String cPath = "/Users/wangzhenqing/git_work/java/c";
        getDirectoryFiles(path, newPath, cPath);
    }
}
