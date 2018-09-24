using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class FPController : MonoBehaviour {

    //Variables
    public float speed = 2.5f;
   // public float jumpspeed = 20f;
    public float sensitivity = 50f;
   // public float height = 10f;
   // public float gravity = .00000002f;
    
    int count = 0;
    public GameObject vision;
    CharacterController player; //stores character controller (see player capsule) in a variable

    float moveFB; //front-back
    float moveLR; //left-right
   // float moveUD; //up-down
    
    
    float rotX; //rotation X
    float rotY; //rotation y
            
    void Start () {

        player = GetComponent<CharacterController>();
	}
	
	// Update is called once per frame
	void Update () {
       
        moveFB = Input.GetAxis("Vertical") * speed; //modifies the vertical (Z Axis) speed
        moveLR = Input.GetAxis("Horizontal") * speed; //modifies the horizontal (X Axis) speed
      //  if(Input.GetKey("space") && player.isGrounded)
      //      moveUD = jumpspeed;

        rotX = Input.GetAxis("Mouse X") * sensitivity; //rotates the camera horizontally based on mouse position
        rotY = Input.GetAxis("Mouse Y") * sensitivity; //rotates the camera Vertically based on mouse position

        Vector3 movement = new Vector3 (moveLR,0,moveFB);
        transform.Rotate(0, rotX, 0);
        if (!Input.GetKeyDown("escape"))
            vision.transform.Rotate(rotY * - 1, 0 , 0);
        movement = transform.rotation * movement;
        player.Move(movement * Time.deltaTime);
        //moveUD -= gravity;
        if (Input.GetKeyDown("escape"))
            Screen.lockCursor = false;
        else
            Screen.lockCursor = true;

    }

}


    


