package application;

import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;

import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.stage.Stage;
import javafx.scene.web.WebView;
import javafx.scene.input.*;
import javafx.scene.layout.*;

public class SpecifyElementController implements Initializable {

    @FXML
    public static Button button_ok; // Value injected by FXMLLoader
    @FXML
    public static TextArea textarea_text; // Value injected by FXMLLoader
    @FXML
    public static Parent root; // Value injected by FXMLLoader
    @FXML
    public static MenuButton menu_initially; // Value injected by FXMLLoader
    @FXML
    public static MenuButton menu_type; // Value injected by FXMLLoader
    @FXML
    public static MenuItem menuitem_text; // Value injected by FXMLLoader
    @FXML
    public static MenuItem menuitem_list; // Value injected by FXMLLoader
    @FXML
    public static MenuItem menuitem_none; // Value injected by FXMLLoader
    @FXML
    public static MenuItem menuitem_collapsed; // Value injected by FXMLLoader
    @FXML
    public static MenuItem menuitem_expanded; // Value injected by FXMLLoader

    @FXML
    public static Pane innerpane_list; // Value injected by FXMLLoader

    @FXML
    public static Pane innerpane_text; // Value injected by FXMLLoader

    @Override
    public void initialize(URL fxmlFileLocation, final ResourceBundle resources)
    {
      if (Globals.specifyListController.isEdit)
      {
         textarea_text.setText(Globals.specifyListController.getElementText());
         String text = Globals.specifyListController.getElementTypeText();

         innerpane_list.setVisible(false);
         innerpane_text.setVisible(false);

         if (text.charAt(0) == 'N')
         {
            menu_type.setText("None");
         }
         else
         {
            if (text.charAt(0) == 'L')
            {
               menu_type.setText("List");
               innerpane_list.setVisible(true);
            }
            else
            {
               menu_type.setText("Text");
               innerpane_text.setVisible(true);
            }

            menu_initially.setText(
               text.charAt(text.length() - 4) == 'd' ? "Expanded" : "Collapsed"
            );
         }
      }
      else
      {
         innerpane_list.setVisible(false);
         innerpane_text.setVisible(true);
      }
      menuitem_none.setOnAction(new EventHandler<ActionEvent>()
      {
         public void handle(ActionEvent event)
         {
            menu_type.setText(menuitem_none.getText());
            innerpane_list.setVisible(false);
            innerpane_text.setVisible(false);

         }
      });
      menuitem_text.setOnAction(new EventHandler<ActionEvent>()
      {
         public void handle(ActionEvent event)
         {
            menu_type.setText(menuitem_text.getText());
            innerpane_list.setVisible(false);
            innerpane_text.setVisible(true);
         }
      });
      menuitem_list.setOnAction(new EventHandler<ActionEvent>()
      {
         public void handle(ActionEvent event)
         {
            menu_type.setText(menuitem_list.getText());
            innerpane_list.setVisible(true);
            innerpane_text.setVisible(false);
         }
      });
      menuitem_collapsed.setOnAction(new EventHandler<ActionEvent>()
      {
         public void handle(ActionEvent event)
         {
            menu_initially.setText(menuitem_collapsed.getText());
         }
      });
      menuitem_expanded.setOnAction(new EventHandler<ActionEvent>()
      {
         public void handle(ActionEvent event)
         {
            menu_initially.setText(menuitem_expanded.getText());
         }
      });

   /*
      buttonpane.setOnMouseClicked(new EventHandler<MouseEvent>()
      {
         public void handle(MouseEvent event)
         {
            clickButtonpane();
         }
      });
*/
      button_ok.setOnAction(new EventHandler<ActionEvent>()
      {
         public void handle(ActionEvent event)
         {
            clickButtonOk();
         }
      });
    }

    public void clickButtonOk()
    {
      String type = menu_type.getText();

      if (!type.equals("None"))
      {
         type += " (" + menu_initially.getText() + ")";
      }

      Globals.specifyListController.setElementAttributes(
         textarea_text.getText(),
         type
      );

      ((Stage)root.getScene().getWindow()).close();
    }
}
