
/**
 * @author:wangzq
 * @email:wangzhenqing1008@163.com
 * @date:2015-06-30 11:01:54
 * @description:将抓取的代码进行代码格式化
 */

import org.eclipse.jdt.core.JavaCore;
import org.eclipse.jdt.core.ToolFactory;
import org.eclipse.jdt.core.formatter.CodeFormatter;
import org.eclipse.jdt.core.formatter.DefaultCodeFormatterConstants;
import org.eclipse.jface.text.Document;
import org.eclipse.jface.text.IDocument;
import org.eclipse.text.edits.TextEdit;

import java.io.*;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Map;


public class JavaCodeFormatUtils {

    /**
     * 调用eclipse jdt core对生成的java源码进行格式化
     * 尝试对传入的JavaSourceFile格式化，此操作若成功则将改变传入对象的内容
     *
     * @author pf-miles 2014-4-16 下午2:48:29
     */
    @SuppressWarnings({"rawtypes", "unchecked"})
    public static String reformatCode(String code, String fileName) {
        String formatCode = "";
        Map m = DefaultCodeFormatterConstants.getEclipseDefaultSettings();
        m.put(JavaCore.COMPILER_COMPLIANCE, 1.6);
        m.put(JavaCore.COMPILER_CODEGEN_TARGET_PLATFORM, 1.6);
        m.put(JavaCore.COMPILER_SOURCE, 1.6);
        m.put(DefaultCodeFormatterConstants.FORMATTER_LINE_SPLIT, "80");
        m.put(DefaultCodeFormatterConstants.FORMATTER_TAB_CHAR, JavaCore.SPACE);

        IDocument doc = null;
        try {
            CodeFormatter codeFormatter = ToolFactory.createCodeFormatter(m);
            TextEdit textEdit = codeFormatter.format(CodeFormatter.K_UNKNOWN, code, 0, code.length(), 0, null);
            if (textEdit != null) {
                doc = new Document(code);
                textEdit.apply(doc);
                formatCode += doc.get() + "\n";
            }
        } catch (Exception e) {
            System.err.println("格式化文件出错" + e);
            e.printStackTrace();
        }
        if ("".equals(formatCode)) {
            System.out.println(fileName);
            return code;
        }
        return formatCode;
    }


    /**
     * @param file
     * @return
     * @Description: 获取文件内容
     * @date 2013-7-11,下午04:30:48
     * @author wangzq
     * @version 3.0.0
     */
    public static String getFileCode(File file) {
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
        int k = 0;
        for (File file : files) { // 删除该文件夹下的文件和文件夹
            String fileName = file.getName();
            String head = getCodeHead(fileName);
            String code = getFileCode(file);
            code = head + code;
            code = reformatCode(code, fileName);
            if ("".equals(code)) {
                System.out.println(fileName);
            }
//            System.out.println(code);
            writeCodeToFile(newPath + File.separator + fileName, code);
            k++;
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
     * 给每个文件增加文件头
     *
     * @param fileName
     * @return
     */
    public static String getCodeHead(String fileName) {
        String probId = fileName.substring(2, 6);
        String probName = fileName.substring(0, fileName.length() - 5);
        SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        String head = "" + "\n";
        head += "" + "\n";
        head += "// " + probName + "\n";
        head += "" + "\n";
        head += "/**" + "\n";
        head += " * @author:wangzq" + "\n";
        head += " * @email:wangzhenqing1008@163.com" + "\n";
        head += " * @date:" + dateFormat.format(new Date()) + "\n";
        head += " * @url:http://ac.jobdu.com/problem.php?pid=" + probId + "\n";
        head += " */" + "\n";
        return head;
    }


    public static void main(String[] args) {
        String path = "/Users/wangzhenqing/git_work/java/test";
        String newPath = "/Users/wangzhenqing/git_work/java/new";
        getDirectoryFiles(path, newPath);
    }
}
