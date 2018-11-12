using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PauseMenu : MonoBehaviour {

    void Start() {
        Cursor.lockState = CursorLockMode.Locked;
        Cursor.visible = false;
}

    private void Update(){
        while (Input.GetKeyDown(KeyCode.Escape)){
            Cursor.lockState = CursorLockMode.None;
            Cursor.visible = true;
        }

       
    }

    void OnApplicationFocus(bool ApplicationIsBack) {
        if (ApplicationIsBack == true) {
            Cursor.lockState = CursorLockMode.Locked;
            Cursor.visible = false;
        }
    }
}
