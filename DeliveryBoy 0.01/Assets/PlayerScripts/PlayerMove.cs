using UnityEngine;
using System.Collections;

// The GameObject is made to bounce using the space key.
// Also the GameOject can be moved forward/backward and left/right.
// Add a Quad to the scene so this GameObject can collider with a floor.

public class PlayerMove : MonoBehaviour
{
    public float speed = 6.0f;
    public float jumpSpeed = 8.0f;
    public float gravity = 20.0f;

    private Vector3 playerMove = Vector3.zero;
    private CharacterController controller;

    void Start(){
        controller = GetComponent<CharacterController>();

        gameObject.transform.position = new Vector3(0, 5, 0);
    }

    void Update(){
        move();
    }

    void move(){

        if (controller.isGrounded)
        {

            playerMove = new Vector3(Input.GetAxis("Horizontal"), 0.0f, Input.GetAxis("Vertical"));
            playerMove = transform.TransformDirection(playerMove);
            playerMove = playerMove * speed;

            if (Input.GetButton("Jump"))
            {
                playerMove.y = jumpSpeed;
            }
        }

        playerMove.y = playerMove.y - (gravity * Time.deltaTime);

        controller.Move(playerMove * Time.deltaTime);
    }
}