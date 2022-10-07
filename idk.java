import javax.swing.*;
import java.awt.*;

public class idk {
    public static void main(String[] args) {
        JFrame frame = new JFrame();
        frame.setName("YouTube Downloader");
        frame.setSize(400,400);
        frame.setVisible(true);

        ImageIcon icon = new ImageIcon("youtube-arrow.png");
        frame.setIconImage(icon.getImage());
        frame.getContentPane().setBackground(new Color(70,70,70));
        String text1 = "Run";
        JButton button1 = new JButton(text1);
        button1.setBounds(50,100,95,30);
        frame.add(button1);
    }
}
