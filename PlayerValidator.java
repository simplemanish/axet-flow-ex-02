package com.ms.player.validator;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Set;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.MessageSource;
import org.springframework.stereotype.Component;
import org.springframework.validation.Errors;
import org.springframework.validation.Validator;

import com.ms.player.form.PlayerForm;
import com.ms.player.model.Player;
import com.ms.player.model.Role;
import com.ms.player.service.PlayerService;
import com.ms.player.service.RoleService;

/**
 * This class responsible for validating player and role.
 * 
 * <p>
 * Validates duplicate player if exists, dob format and if role not exists.
 * </p>
 * 
 * Please see the {@link com.ms.player.validator.PlayerValidator} class
 * 
 * @author 047929
 * @version 1.0.0
 */
@Component
public class PlayerValidator implements Validator {
	/**
	 * Player service.
	 */
	@Autowired
	private PlayerService playerService;
	
	/**
	 * Role service.
	 */
	@Autowired
	private RoleService roleService;

	/**
	 * Message source to get language specific messages.
	 */
	@Autowired
	private MessageSource messageSource;

	Logger logger = LoggerFactory.getLogger(PlayerValidator.class);

	/**
	 * Supported class PlayerForm.
	 */
	@Override
	public boolean supports(Class<?> aClass) {
		return PlayerForm.class.equals(aClass);
	}

	/**
	 * Validates duplicate player if exists, dob format and if role not exists.
	 */
	@Override
	public void validate(Object o, Errors errors) {
		PlayerForm playerForm = (PlayerForm) o;

		// dob format check yyyy-MM-dd
		SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd");
		dateFormat.setLenient(false);

		try {
			dateFormat.parse(playerForm.getDob());
		} catch (ParseException e) {
			errors.rejectValue("dob", "", messageSource.getMessage("validation.date.format", null, null));
		}

		// existing user firstname, lastname and dob should not be same
		Player player = playerService.findPlayerByNameAndDob(playerForm.getFirstname(), playerForm.getLastname(),
				playerForm.getNationality());
		if (null != player) {
			errors.rejectValue("firstname", "", messageSource.getMessage("validation.player.duplicate", null, null));
		}

		// invalid role id
		Set<Long> roleIds = playerForm.getRoles();
		for (Long id : roleIds) {
			Role role = roleService.getRoleById(id);
			if (role == null) {
				errors.rejectValue("roles", "", messageSource.getMessage("validation.role.id", null, null));
				break;
			}
		}

	}

}
